import threading
import requests
import json

'''
The IPThread constructor creates a thread which sends a GET request to the
ip2country API with the IP passed to it as a parameter; parses the response for
the country name of the IP, sends this name back to the callback passed to it,
and prints the IP searched and country name retrieved.
'''

class IPThread(threading.Thread):
    def __init__(self, ip, callback):
        threading.Thread.__init__(self)
        self.ip = ip
        self.callback = callback

    def run(self):
        print "Search:", self.ip
        response = requests.get("http://api.ip2country.info/ip?" + self.ip)
        country_name = json.loads(response.text)['countryName']
        self.callback(country_name)
        print "countryName:", country_name
