#!/usr/bin/ruby

require 'httpclient'

filename = 20
filepath = '/tmp/20'
extheaders = {
  'User-Agent' => 'Holberton School',
  'Authorization' => 'token a2eaac77d1b665a2f1fea8ce17cd48178cd21a69'
}

http_request = HTTPClient.new
File.write(filepath, http_request.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc', query = nil, extheaders))
