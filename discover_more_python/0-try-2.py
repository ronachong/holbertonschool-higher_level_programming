#!/usr/bin/python

import urllib
import urllib2

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'
#null = urllib.urlencode({})
#request_headers = {
#      'User-Agent': 'Holberton_School',
#      'Authorization': 'token a2eaac77d1b665a2f1fea8ce17cd48178cd21a69'
#    }
#req = urllib2.Request(url, null, request_headers)
response = urllib2.urlopen(url)

print response.read()
