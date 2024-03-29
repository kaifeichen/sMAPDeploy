# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2
"""
Copyright (c) 2011, 2012, Regents of the University of California
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions 
are met:

 - Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
 - Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the
   distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS 
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
OF THE POSSIBILITY OF SUCH DAMAGE.
"""
"""
@author Andrew Krioukov
@author Stephen Dawson-Haggerty
"""

import sys
sys.path.insert(0, '/home/oski/bacnet/')
from operator import itemgetter
from pybacnet import bacnet
import optparse
import json

def process_point(dev, obj):
  # Special cases for different control systems

  # WattStopper relays
  if dev.startswith('WS') and \
    (obj.startswith('RELAY') or obj.startswith('GROUP')):
    return bacnet.BACNET_APPLICATION_TAG_ENUMERATED
  # Siemens
  elif obj == 'HEAT.COOL':
    return bacnet.BACNET_APPLICATION_TAG_ENUMERATED
  else:
    return bacnet.BACNET_APPLICATION_TAG_REAL

def main():
  parser = optparse.OptionParser()
  parser.add_option('-i', '--interface', dest='interface',
                    default=None,
                    help='Network interface to broadcast over')
  parser.add_option('-p', '--ip-filter', dest='fip', default=None,
                    help='Filter devices by IP prefix')

  opts, args = parser.parse_args()
  if len(args) != 1:
    print "Usage:", sys.argv[0], "[options] <output file>"
    parser.print_help()
    sys.exit(1)

  filename = args[0]
  fout = open(filename, 'wb')

  # MUST USE default port for whois
  bacnet.Init(opts.interface, None)

  device_list = []
  # Discover and store devices
  devs = bacnet.whois(5)
  print >>sys.stderr, "Found", len(devs), "devices"

  for h_dev in sorted(devs, key=itemgetter('device_id')):
    # IP filter
    mac = '.'.join([str(i) for i in h_dev['mac']])
    if not opts.fip or mac.startswith(opts.fip):
      # Dev filter
      objs = []
      obj_count = bacnet.read_prop(h_dev, bacnet.OBJECT_DEVICE, h_dev['device_id'], bacnet.PROP_OBJECT_LIST, 0)
      name = bacnet.read_prop(h_dev, bacnet.OBJECT_DEVICE, h_dev['device_id'], bacnet.PROP_OBJECT_NAME, -1)
      try:  
        desc = bacnet.read_prop(h_dev, bacnet.OBJECT_DEVICE, h_dev['device_id'], bacnet.PROP_DESCRIPTION, -1)
      except IOError:
        desc = None

      device = {
        'props': h_dev,
        'name': name,
        'desc': desc,
        'objs': []
        }

      if obj_count == 0:
        print >>sys.stderr, "No objects found:", d
        continue 

      # Get object props and names
      for i in range(1, obj_count+1):
        h_obj = bacnet.read_prop(h_dev, bacnet.OBJECT_DEVICE, h_dev['device_id'], bacnet.PROP_OBJECT_LIST, i)
        if h_obj == None:
          print >>sys.stderr, "Object not found:", i 
          continue
        try:
          name = bacnet.read_prop(h_dev, h_obj['type'], h_obj['instance'], bacnet.PROP_OBJECT_NAME, -1)
        except IOError:
          name = None
        try:
          desc = bacnet.read_prop(h_dev, h_obj['type'], h_obj['instance'], bacnet.PROP_DESCRIPTION, -1)
        except IOError:
          desc = None
        try:
          unit = bacnet.read_prop(h_dev, h_obj['type'], h_obj['instance'], bacnet.PROP_UNITS, -1)
        except IOError:
          unit = None

        device['objs'].append({
          'props': h_obj,
          'name': name,
          'desc': desc,
          'unit': unit,
          'data_type': process_point(device['name'], name),
          })
      print >>sys.stderr, device['name'], "has", len(device['objs']), "objects"
      device_list.append(device)
  json.dump(device_list, fout)
  fout.close()

if __name__ == "__main__":
  main()
