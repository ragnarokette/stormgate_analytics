import csv
import pandas as pd

matches = pd.read_csv("20240206_matches.csv")
player_matches = pd.read_csv("20240206_player_matches.csv")
players = pd.read_csv("20240206_players.csv")

result = pd.merge(player_matches, players, on="player_id")

