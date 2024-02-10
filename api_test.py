import requests
import csv
import time
from datetime import datetime

url = 'https://api.stormgateworld.com/v0/matches'
page = 1
total_players = 0

filename = 'matches_' + datetime.now().strftime("%Y%m%d_%H%M") + '.csv'
filename2 = 'player_matches_' + datetime.now().strftime("%Y%m%d_%H%M") + '.csv'

with open('results/' + filename, 'w', newline='', encoding='utf-8') as csvfile:
    with open('results/' + filename2, 'w', newline='', encoding='utf-8') as csvfile2:
        csv_writer = csv.writer(csvfile)
        csv_writer_pm = csv.writer(csvfile2)
        csv_writer.writerow([
                            "match_id",
                            'state',
                            "leaderboard",
                            "server",
                            "created_at",
                            "ended_at",
                            "duration"
                            ])
        csv_writer_pm.writerow([
                            "match_id",
                            "player_id",
                            "race",
                            'team',
                            "mmr",
                            "mmr_updated",
                            "mmr_diff",
                            "result",
                            "ping",
                            'xp',
                            'units_killed',
                            'resources_mined',
                            'structures_killed',
                            'creep_resources_collected',
                            ])
        while page + 1 < total_players / 100 or page == 1:
            time.sleep(1)
            params = {'page': page}
            response = requests.get(url, params=params)
            r = response.json()
            total_players = r['total']
            print('Page: ' + str(page) + ' for ' + str(total_players) + ' total matches')
            for match in r['matches']:
                csv_writer.writerow([
                    match['match_id'],
                    match['state'],
                    match['leaderboard'],
                    match['server'],
                    match['created_at'],
                    match['ended_at'],
                    match['duration']
                ])
                for player in match['players']:
                    if 'player' not in player.keys():
                        player['player'] = {'player_id': None}
                    if player['scores'] is None:
                        player['scores'] = {
                            'xp': None,
                            'units_killed': None,
                            'resources_mined': None,
                            'structures_killed': None,
                            'creep_resources_collected': None,
                        }
                    csv_writer_pm.writerow([
                        match['match_id'],
                        player['player']['player_id'],
                        player['race'],
                        player['team'],
                        player['mmr'],
                        player['mmr_updated'],
                        player['mmr_diff'],
                        player['result'],
                        player['ping'],
                        player['scores']['xp'],
                        player['scores']['units_killed'],
                        player['scores']['resources_mined'],
                        player['scores']['structures_killed'],
                        player['scores']['creep_resources_collected']
                    ])
            page += 1