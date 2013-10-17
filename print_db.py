import sys
import json
import pprint

if len(sys.argv) != 2:
	print "Usage: %s <database>" % sys.argv[0]
	sys.exit(1)

data = json.load(open(sys.argv[1]))

#pprint.pprint(data)

for dev in sorted(data, key=lambda d: d['name']):
	print "Device: %s, %s, %s, %s" % (dev['name'], dev['props']['device_id'], dev['desc'], len(dev['objs']))
	for obj in sorted(dev['objs'], key=lambda o: o['name']):
		print "\t %s, %s" % (obj['name'], obj['desc'])
