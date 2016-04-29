#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    medallion = line.strip().split('\t')[0].strip().split(',')[0]
    datetime = line.strip().split('\t')[0].strip().split(',')[3].strip().split()[0]

    print '%s\t%s,%d' %(medallion, datetime, 1)