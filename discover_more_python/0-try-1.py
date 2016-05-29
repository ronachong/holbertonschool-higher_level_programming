#!/usr/bin/python

import httplib

request_headers = {
      'User-Agent': 'Holberton_School',
      'Authorization': 'token a2eaac77d1b665a2f1fea8ce17cd48178cd21a69'
    }

conn = httplib.HTTPConnection("api.github.com")
conn.request("GET", "/search/repositories?q=language:python&sort=stars&order=desc", "", request_headers)
response = conn.getresponse()
data = response.read()
print data
conn.close()
