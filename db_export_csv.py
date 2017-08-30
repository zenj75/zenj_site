#!/bin/env python
#
# экспорт (выгрузка) таблицы из db.sqlite3  в CSV (backup)

import json
import sqlite3
import csv

try:
	con = sqlite3.connect('db.sqlite3')
except:
	print('bzz')

with con:
	cur = con.cursor()
	cur.execute("select * from main_app_work;")

# with open('db.json', 'w') as f:
# 	json.dump(cur, f)

with open("db_dump.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cur.description])  #write headers
    csv_writer.writerows(cur)

