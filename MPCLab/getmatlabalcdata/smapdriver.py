
# -*- coding: utf8 -*-
##########################################################
# load data -> JSON format -> Post to the server
##########################################################
# Dezhi Hong and Kaifei Chen

import csv
import glob
import time
import datetime
import urllib
import json
import httplib
import uuid
# import simplejson
# import pickle

dataQueue = [100, 200]
uid = uuid.uuid1()

host = 'new.openbms.org'
url = '/add'
key = 'mQTzpoir9QUNe7VvXdGW8i8LgN7cdtRw0zCx' #Kaifei's key
port = 8079
headers = {'Content-Type':'application/json', 'Connection':'Keep-Alive', 'Referer':host} 


with open('MPCtrends.csv', 'rb') as trendsf:
  trends = csv.reader(trendsf, delimiter=',')
  tnum = 0

  for t in trends:
    if tnum > 0:
      uid = uuid.uuid1()

      datafiles = glob.glob('data/'+str(tnum)+'/*.csv')
      for datafile in datafiles:
        with open(datafile, 'rb') as dataf:
          readings = csv.reader(dataf, delimiter=',')
          readings = [(int(time.mktime(time.strptime(reading[0], "%m/%d/%y %H:%M:%S")))*1000, float(reading[1])) for reading in readings if 'NaN' not in reading[1]]

          ts = {
            '/'+t[2] : {
              'Metadata':{
                'SourceName': 'Model Predictive Control Lab',
                'Instrument': {
                  'Manufacturer': t[1]
                },
                'Location':{
                  'City': 'Berkeley', 
                  'Building': 'Etcheverry Hall',
                  'Campus': 'UC Berkeley',
                  'Country': 'US',
                  'Floor': '2nd Floor',
                  'Room': '2169',
                  'Street': 'Hearst Ave'
                },
                'Extra':{
                  'Name': t[2],
                  'Type': t[3]
                }
              },
              'Properties':{
                'TimeZone':'US/Los_Angeles',
                'ReadingType':'double'
              },
              'Readings' : readings,
              'uuid' : str(uid)
            }
          }

          # ts = {
          #   "/sensor0/ww" : {
          #     "Metadata" : {
          #       "SourceName" : "Model Predictive Control Lab",
          #       "Location" : { "City" : "Berkeley" }
          #     },
          #     "Properties": {
          #       "Timezone": "America/Los_Angeles",
          #       "UnitofMeasure": "Watt",
          #       "ReadingType": "double"
          #     },
          #     "Readings" : [[1351043674000, 0], [1351043675000, 1]],
          #     "uuid" : "d24325e6-1d7d-11e2-ad69-a7c2fa8dba62"
          #   }
          # }

          jdata = json.dumps(ts)
          print  jdata

          conn = httplib.HTTPConnection(host, port)
          conn.request(method='POST', url= url + '/' + key, body=jdata, headers=headers)
          response = conn.getresponse()
          print tnum, datafile
          print 'status:', response.status

          conn.close()
          
    tnum = tnum + 1

      
