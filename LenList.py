import mysql.connector
from lokalhost_entry import passwd, user_pantry

pantry_db = mysql.connector.connect(host="localhost", user=user_pantry, passwd=passwd, database="mypantry")
pantry_cursor = pantry_db.cursor()

pantry_cursor.execute("select * from mypantry.products_items")
all_db_pantry = pantry_cursor.fetchall()

len_all_pantry =[]

for i in range(len(all_db_pantry)):
    len_all_pantry.append(i)

name_all_pantry = []

for index, name in enumerate(all_db_pantry):
    name_all_pantry.append(name[1])


# for i in name_all_pantry:
#     print(type(i), i)
