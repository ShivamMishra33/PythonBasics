import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
add = 0
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
info = json.loads(data)
print('User count:', len(info))
lis = info['comments']
for sec in lis:
    add += int(sec['count'])

print(add)




