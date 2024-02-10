import csv
import sqlite3

con = sqlite3.connect("C:\Program Files\SQLiteStudio\Stormgate")

cur = con.cursor()

cur.execute("drop table if exists players")