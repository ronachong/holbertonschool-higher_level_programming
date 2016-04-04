#!/usr/bin/python

import urllib2
import json

# create HTTP request
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
request_headers = {
      'User-Agent': 'Holberton_School',
      'Authorization': 'token a2eaac77d1b665a2f1fea8ce17cd48178cd21a69'
    }
req = urllib2.Request(url, None, request_headers)
response = urllib2.urlopen(req)

# parse jsonstring response into python dict
jsonstring = response.read()

json_as_dict = json.loads(jsonstring) # I believe this should be ALL of the data from the URL, but there are whole chunks missing within items. Why?
items = json_as_dict['items'] # Chunks still missing.
idk = items[0] # Looks really weird.

print(jsonstring)

response.close()
