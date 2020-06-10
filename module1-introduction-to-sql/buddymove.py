import sqlite3
import os
import pandas as pd

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")
print(DB_FILEPATH)

# df.to_sql

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv')
df.to_sql('Review', con=connection)
results = cursor.execute("SELECT * FROM Review").fetchall()
print(results)

#query = SELECT COUNT(*) FROM Review