# Coordinate class to get coordinates from google MAP API
# Output will be fed to forecast.io api for weather information
# Requests plugin is required and is used for HTTP requests
# Author: Bhaumik Shah
# Python version used: 2.7.10
# Project URL to fork: https://github.com/shahbhaumik/smart_thermostat.git
# Usage and Wiki at: https://github.com/shahbhaumik/smart_thermostat/wiki

import requests


class Coordinates:
    # Initializing coordinate class
    def __init__(self, address_line1, city, state):
        self.address = address_line1
        self.city = city
        self.state = state
        self.lat = 0
        self.lng = 0

    # using request for python getting lat and lng for the given address
    def get_geocode(self):
        payload = {'address': self.address + self.city + self.state, 'key': ''}
        r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?', params=payload)
        print (r.url)
        geo_code = r.json()
        self.lat = geo_code[u'results'][0][u'geometry'][u'location'][u'lat']
        self.lng = geo_code[u'results'][0][u'geometry'][u'location'][u'lng']
        print self.lat, self.lng





