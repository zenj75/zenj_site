#!/bin/env python 
#
# небольшой скрипт по занесению (import) данных из csv в базу django  (таблица Work)

import os
import sys
import csv
from pandas import read_csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)

from main_app.models import Work

with open('db_data.csv', 'r') as csv_file:
	out = read_csv(csv_file, sep=',', skiprows=[0], header=None)

for i in range(len(out[0])):
    w = Work()
    w.wname = out[1][i]
    w.prof = out[2][i]
    w.wdescr = out[3][i]
    w.order = out[5][i]
    w.save()



