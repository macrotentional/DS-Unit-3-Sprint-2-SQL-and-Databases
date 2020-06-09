import sqlite3
import os
import pandas as pd

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")

# df.to_sql

#from sqlalchemy import create_engine
#engine = create_engine('sqlite://', echo=False)
#df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv')
#df.to_sql('Review', con=engine)
#engine.execute("SELECT * FROM Review").fetchall()

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = SELECT COUNT(*) FROM Review