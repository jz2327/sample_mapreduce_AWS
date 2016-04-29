#!/usr/bin/python

import sys
import csv
import StringIO

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    line_split_t = line.strip().split('\t')
    csv_file = StringIO.StringIO(line_split_t[1])
    csv_reader = csv.reader(csv_file)
    for record in csv_reader:
        vehicle_type = record[25]
        fare_amount = float(record[14])
        surcharge_amount = float(record[15])
        tips_amount = float(record[17])
        revenue = fare_amount+surcharge_amount+tips_amount
        if revenue == 0:
            print '%s\t%.2f,%.2f,%d' %(vehicle_type, 0, 0, 1)
        else:
            percentage_tips = tips_amount/revenue
            print '%s\t%.2f,%.2f,%d' %(vehicle_type, revenue, percentage_tips, 1)

        


