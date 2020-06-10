import os
from dotenv import load_dotenv
import psycopg2

load_dotenv() #> loads contents of the .env file into the script's environment

#use env vars DON'T COMMIT YET!!!
DB_NAME = 'wcycyfre'
DB_USER = 'wcycyfre'
DB_PASSWORD = 'Gl7IX-LiLtibUHOuy8uIJL6C5hMf_xYX'
DB_HOST = 'hansken.db.elephantsql.com'

### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname='wcycyfre', user='wcycyfre',
                        password='Gl7IX-LiLtibUHOuy8uIJL6C5hMf_xYX', host='hansken.db.elephantsql.com')
print("CONNECTION:", connection)
### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()
print("CURSOR:", cursor)
### An example query
cursor.execute('SELECT * from charactercreator_necromancer;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cursor.fetchone()
#result = cursor.fetchall()
print("RESULT:", type(result))
print(result)