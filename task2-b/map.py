#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    line_str = line.strip()
    total_amount = float(line_str.split('\t')[1].strip().split(',')[16])

    if total_amount <= 10:
        print '%s\t%d' %('key', 1)


