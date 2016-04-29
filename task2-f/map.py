#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    medallion = line.strip().split('\t')[0].strip().split(',')[0]
    driver = line.strip().split('\t')[0].strip().split(',')[1]

    print '%s\t%s' %(driver, medallion)