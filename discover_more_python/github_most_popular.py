#!/usr/bin/python

import urllib2

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
request_headers = {
      'User-Agent': 'Holberton_School',
      'Authorization': 'token a2eaac77d1b665a2f1fea8ce17cd48178cd21a69'
    }
req = urllib2.Request(url, None, request_headers)
response = urllib2.urlopen(req)

print response.read()
response.close()
