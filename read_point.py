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

import json
import sys
import os
#sys.path.insert(0, '/Users/Andrew/BACnet')

from pybacnet import bacnet


def load(db_file):
  with open(db_file, 'r') as fp:
    return json.load(fp)

def find(devices, obj_name, dev_name = None):
  for d in devices:
    if not dev_name or d['name'] == dev_name:
      for o in d['objs']:
        if o['name'] == obj_name:
          return (d, o)
  return (None, None)

def main():
  if len(sys.argv) == 3:
    db = sys.argv[1]
    obj_name = sys.argv[2]
    dev_name = None
  elif len(sys.argv) == 4:
    db = sys.argv[1]
    obj_name = sys.argv[2]
    dev_name = sys.argv[3]
  else:
    print "Usage: read_point.py db_file obj_name [dev_name]"
    sys.exit(1)

  devices = load(db)
  bacnet.Init('eth0', None)

  (dev, obj) = find(devices, obj_name, dev_name) 
  if dev == None:
    print "Point not found"
    sys.exit(1)

  #print "Reading: ", dev['props'], obj['props']
  print bacnet.read_prop(dev['props'], obj['props']['type'], obj['props']['instance'], bacnet.PROP_PRESENT_VALUE, -1)

if __name__ == '__main__':
  main()
