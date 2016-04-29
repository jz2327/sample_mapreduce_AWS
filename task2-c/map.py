#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    line_str = line.strip()
    passenger_count = float(line_str.split('\t')[1].strip().split(',')[3])

    if passenger_count == 0:
        print '%s\t%d' %('0', 1)
    if passenger_count == 1:
        print '%s\t%d' %('1', 1)
    if passenger_count == 2:
        print '%s\t%d' %('2', 1)
    if passenger_count == 3:
        print '%s\t%d' %('3', 1)
    if passenger_count == 4:
        print '%s\t%d' %('4', 1)
    if passenger_count == 5:
        print '%s\t%d' %('5', 1)
    if passenger_count == 6:
        print '%s\t%d' %('6', 1)

