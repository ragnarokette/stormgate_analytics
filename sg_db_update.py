import sqlite3
import pandas as pd

con = sqlite3.connect("StormgateDB")

cur = con.cursor()

#update players table
cur.execute("delete from players;")
players_df = pd.read_csv('results/players_20240215_0208.csv', encoding='utf-8')
players_df.to_sql('players', con, if_exists='append', index=False)

#update matches table
matches_df = pd.read_csv('results/matches_20240215_0153.csv', encoding='utf-8')
matches_df.to_sql('matches', con, if_exists='append', index=False)

#update player_matches table
pm_df = pd.read_csv('results/player_matches_20240215_0153.csv', encoding='utf-8')
pm_df.to_sql('player_matches', con, if_exists='append', index=False)

con.commit()
con.close()