import threading
import requests
import json

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
