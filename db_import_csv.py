#!/bin/env python 
#
# небольшой скрипт по занесению (import) данных из csv в базу django

import os
import sys
import csv
from pandas import read_csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
# from django.core.management import execute_from_command_line
# execute_from_command_line(sys.argv)

from main_app.models import School

with open('db_data.csv', 'r') as csv_file:
	out = read_csv(csv_file, sep=';', skiprows=[0], header=None)

# for i in range(len(out[0])):
#     w = Work()
#     w.wname = out[1][i]
#     w.prof = out[2][i]
#     w.wdescr = out[3][i]
#     w.order = out[5][i]
#     w.save()

for i in range(len(out[0])):
    s = School()
    s.lname = out[1][i]
    s.course = out[2][i]
    s.site = out[3][i]
    s.order = out[4][i]
    s.save()

    print(s.lname)
    print(s.course)
    print(s.site)
    print(s.order)

