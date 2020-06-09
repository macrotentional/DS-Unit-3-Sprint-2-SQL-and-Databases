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

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

# Queries
### How many total characters are there?
query = SELECT count() FROM "charactercreator_character"
result = len(cursor.execute(query).fetchall())
print("total characters:", result) # Based on character_id, there are 302 total characters.

### How many of each specific subclass?
query2 = SELECT count() FROM charactercreator_cleric # 75 clerics
result2 = len(cursor.execute(query2).fetchall())
print("total clerics:", result2)

query3 = SELECT count() FROM charactercreator_fighter # 68 fighters
result3 = len(cursor.execute(query3).fetchall())
print("total fighters:", result3)

query4 = SELECT count() FROM charactercreator_cleric # 108 mages
result4 = len(cursor.execute(query4).fetchall())
print("total mages:", result4)

query5 = SELECT count() FROM charactercreator_necromancer # 11 necromancers
result5 = len(cursor.execute(query5).fetchall())
print("total necromancers:", result5)

query6 = SELECT count() FROM charactercreator_thief # 51 thieves
result6 = len(cursor.execute(query6).fetchall())
print("total thieves:", result6)

### How many total items?
query7 = SELECT count() FROM armory_item # 174 total items
result7 = len(cursor.execute(query7).fetchall())
print("total items:", result7)

### How many of the items are weapons? How many are not?
query8 = SELECT count() FROM armory_weapon # 37 weapons
result8 = len(cursor.execute(query8).fetchall())
print("total weapons:", result8)

query9 = SELECT(SELECT COUNT(item_id) FROM armory_item)
- (SELECT COUNT(item_ptr_id) FROM armory_weapon) # 137 non-weapons
result9 = len(cursor.execute(query9).fetchall())
print("total weapons:", result9)

### How many items does each character have? (Return first 20 rows)
query10 = SELECT character_id, COUNT(item_id) as total_items
FROM charactercreator_character_inventory
GROUP BY character_id
#LIMIT 20
result10 = len(cursor.execute(query10).fetchall())
print("Items per character:", result10.head(20))

### How many Weapons does each character have? (Return first 20 rows)
query11 = SELECT character_id, COUNT(item_id) as total_items
FROM charactercreator_character_inventory
WHERE item_id > 137
GROUP BY character_id
#LIMIT 20
result11 = len(cursor.execute(query11).fetchall())
print("Weapons per character:", result11.head(20))

### On average, how many Items does each character have?
query12 = SELECT AVG(items_per_character)
FROM 
(SELECT charactercreator_character.character_id,
COUNT(charactercreator_character_inventory.item_id) AS items_per_character
FROM charactercreator_character
LEFT JOIN charactercreator_character_inventory
ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
GROUP BY charactercreator_character_inventory.character_id) # average of 2.97 items per character
result12 = cursor.execute(query12).fetchall()
print("Items per character:", result12)

### On average, how many Weapons does each character have?
# query13 = SELECT AVG(items_per_character)
# FROM 
# (SELECT charactercreator_character.character_id,
# COUNT(charactercreator_character_inventory.item_id WHERE charactercreator_character_inventory.item_id > 137) AS weapons_per_character
# FROM charactercreator_character
# LEFT JOIN charactercreator_character_inventory
# ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
# GROUP BY charactercreator_character_inventory.character_id)
# result13 = cursor.execute(query13).fetchall()
# print("Weapons per character:", result13)