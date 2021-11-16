# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
count = int(input('Enter count:'))
pos = int(input("Enter position:"))
names_list = []
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    position = 0
    for tag in tags:
        if position == (pos - 1):
            url = tag.get('href', None)
            name = url.split('/')[3].rstrip('.html').lstrip('known_by_')
            names_list.append(name)
            position += 1
        else:
            position += 1

print('Sequence of the names:', end=' ')
for name in names_list:
    print(name,end=' ')

print("\nLast name in sequence:", names_list[count - 1])
