import requests
import csv
import time
from datetime import datetime

url = 'https://api.stormgateworld.com/v0/leaderboards/ranked_1v1'
page = 1
total_players = 0
filename = 'players_' + datetime.now().strftime("%Y%m%d_%H%M") + '.csv'

with open('results/' + filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([
                        "leaderboard_entry_id",
                        "leaderboard",
                        "player_id",
                        "anonymous",
                        "nickname",
                        "nickname_discriminator",
                        "rank",
                        "race",
                        "league",
                        "tier",
                        "mmr",
                        "max_confirmed_mmr",
                        "points",
                        "wins",
                        "losses",
                        "ties",
                        "matches",
                        "win_rate"
                        ])
    while page + 1 < total_players / 100 or page == 1:
        time.sleep(1)
        params = {'page': page}
        response = requests.get(url, params=params)
        r = response.json()
        total_players = r['total']
        print('Page: ' + str(page) + ' for ' + str(total_players) + ' total players')
        for player in r['entries']:
            csv_writer.writerow(list(player.values()))
        page += 1