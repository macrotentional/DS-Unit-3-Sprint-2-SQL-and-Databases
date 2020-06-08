import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "module1-introduction-to-sql/chinook.db"
#DB_FILEPATH = os.path.join("module1-introduction-to-sql", "chinook.db")
#DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module2-0...", "chinook.db")
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = "SELECT * FROM customers;"

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall()
print("RESULT 2", result2)

for row in result2:
    print(type(row), row)

# Queries
```How many total characters are there?```
query = SELECT * FROM  "charactercreator_character_inventory" ORDER BY "character_id" DESC
# Based on character_id, there are 302 total total characters.

```How many of each specific subclass?```
query2 = SELECT count() FROM charactercreator_cleric # 75 clerics
query3 = SELECT count() FROM charactercreator_fighter # 68 fighters
query4 = SELECT count() FROM charactercreator_cleric # 108 mages
query5 = SELECT count() FROM charactercreator_necromancer # 11 necromancers
query6 = SELECT count() FROM charactercreator_thief # 51 thieves

```How many total Items?```
query7 = SELECT count() FROM armory_item # 174 total items

```How many of the Items are weapons? How many are not?```
query8 = SELECT count() FROM armory_weapon # 37 weapons
query9 = SELECT(SELECT COUNT(item_id) FROM armory_item)
- (SELECT COUNT(item_ptr_id) FROM armory_weapon) # 137 non-weapons

```How many Items does each character have? (Return first 20 rows)```
query10 = SELECT character_id, COUNT(item_id) as total_items
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20

```How many Weapons does each character have? (Return first 20 rows)```
query11 = SELECT character_id, COUNT(item_id) as total_items
FROM charactercreator_character_inventory
WHERE item_id > 137
GROUP BY character_id
LIMIT 20

```On average, how many Items does each character have?```
SELECT AVG(item_id) as average_items
FROM charactercreator_character_inventory # average of 89.2 items per character

```On average, how many Weapons does each character have?```



#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result3 = cursor.execute(query).fetchone()
print("RESULT 2", type(result3), result3)