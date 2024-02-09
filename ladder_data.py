#now that I can filter the requests on a time range I can:
#get the last pull time programatically somehow (probably by just doing it daily with a cronjob idk?)
#modify the code from api_test to only pull things in the right date range
#finally, figure out a way to update the tables


import requests
import csv
import time
from dateutil import parser
from datetime import datetime

url = 'https://api.stormgateworld.com/v0/matches'
page = 1
total_players = 0

filename = 'matches_' + datetime.now().strftime("%Y%m%d_%H%M") + '.csv'
filename2 = 'player_matches_' + datetime.now().strftime("%Y%m%d_%H%M") + '.csv'

params = {'page': page}
response = requests.get(url, params=params)
r = response.json()
total_players = r['total']
created_at = ''

last_pulled = datetime(2024, 2, 6, 21, 19, 0)
print(last_pulled)
print('Page: ' + str(page) + ' for ' + str(total_players) + ' total matches')

for match in r['matches']:
    print(match['cached_at'])
    datetime_obj = parser.parse(match['cached_at'])
    