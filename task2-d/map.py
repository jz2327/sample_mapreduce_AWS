#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    line_str = line.strip().split('\t')[1].strip().split(',')
    key_datetime = line.strip().split('\t')[0].strip().split(',')[3].split(' ')[0]
    fare_amount = float(line_str[11])
    surcharge = float(line_str[12])
    tip_amount= float(line_str[14])
    tolls_amount = float(line_str[15])
    revenue = fare_amount+surcharge+tip_amount

    print '%s\t%.2f,%.2f' %(key_datetime, revenue, tolls_amount)