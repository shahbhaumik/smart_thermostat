# Integrating thinkspeak api to get sensor input and commands from user
# There are two class in this file, one that collects data and other gets the command
# Requests plugin is required and is used for HTTP requests
# Author: Bhaumik Shah
# Python version used: 2.7.10
# Project URL to fork: https://github.com/shahbhaumik/smart_thermostat.git
# Usage and Wiki at: https://github.com/shahbhaumik/smart_thermostat/wiki

import requests


class temp_data:

    def __init__(self, Nrooms, API_KEY, Channel_ID):
        self.number = Nrooms
        self.API_KEY = API_KEY
        self.Room = list()
        self.channel_ID = Channel_ID
        for number in range(0,self.number):
            self.Room.append(number)

    def update_room_temp(self):
        payload = {'api_key': self.API_KEY}
        r = requests.get("https://api.thingspeak.com/channels/" + self.channel_ID + "/feeds/last.json", params=payload)
        json_data = r.json()
        if len(self.Room) == 1:
            self.Room[0] = json_data[u'field1']
 #           self.Room[0] = json_data["u'field2"]
 #           self.Room[0] = json_data["u'field3"]



