#!/usr/bin/python

import urllib2

# create empty file '20' in tmp
file = open('/tmp/20', 'a')

# create HTTP request
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
request_headers = {
      'User-Agent': 'Holberton_School',
      'Authorization': 'token a2eaac77d1b665a2f1fea8ce17cd48178cd21a69'
    }
req = urllib2.Request(url, None, request_headers)
response = urllib2.urlopen(req)

# write response to /tmp/20
file.write(response.read())
