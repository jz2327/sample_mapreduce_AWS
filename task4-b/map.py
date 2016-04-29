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
        agent_name = record[29]
        fare_amount = float(record[14])
        surcharge_amount = float(record[15])
        tips_amount = float(record[17])
        revenue = fare_amount+surcharge_amount+tips_amount

        print '%s\t%s' %(agent_name, revenue)


