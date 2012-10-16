#!/usr/bin/python2
import urllib2
import base64
import json
import datetime

username = "jsonapi"
password = "AhVai6OoCh3Quoo6ji"
theurl = 'https://www.studentenwerk-karlsruhe.de/json_interface/canteen/'

req = urllib2.Request(theurl)
base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
req.add_header("Authorization", "Basic %s" % base64string)

try:
    handle = urllib2.urlopen(req)
except IOError, e:
    if hasattr(e, 'code'):
        if e.code != 401:
            print 'We got another error'
            print e.code
        else:
            print e.headers
            print e.headers['www-authenticate']

mensaplan = json.loads(handle.read())

## pretty-print json
#print json.dumps(mensaplan['moltke'], sort_keys=True, indent=4)
#print mensaplan['moltke']

## Print timestampes
#for item in sorted(mensaplan['moltke'].keys()):
#   print(datetime.datetime.fromtimestamp(int(item)).strftime('%Y-%m-%d'))

timestamps = sorted(mensaplan['moltke'].keys())
linien = ['wahl1', 'wahl2', 'aktion', 'gut', 'schnitzelbar', 'buffet']

print (datetime.datetime.fromtimestamp(int(timestamps[3])).strftime('%Y-%m-%d'))
# loop over lines
for line in linien:
    print "******************"
    current_line = mensaplan['moltke'][timestamps[1]][line]
    print line    
    print "******************"
    # loop over meals in on line
    for meal in current_line:
        print meal['meal'] +' '+ meal['dish']+' '+meal['info']
    print ""
