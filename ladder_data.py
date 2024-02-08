import csv
import pandas as pd
from pandasql import sqldf

matches = pd.read_csv("20240206_matches.csv")
#player_matches has two entries, one for each player in a match
player_matches = pd.read_csv("20240206_player_matches.csv")
players = pd.read_csv("20240206_players.csv")

print(player_matches.shape)
print(sqldf('''
            drop table if exists retained_players;
            create temp table retained_players as(
            select * 
            from player_matches
            where player_race_match_num > 10);
           
            select * from retained_players limit 1;
            '''))