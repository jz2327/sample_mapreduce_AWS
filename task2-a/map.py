#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    line_str = line.strip()
    fare_amount = float(line_str.strip().split('\t')[1].strip().split(',')[11])

    if fare_amount >=0 and fare_amount <=4:
        print '%s\t%d' %('0,4', 1)
    if fare_amount >=4.01 and fare_amount <=8:
        print '%s\t%d' %('4.01,8', 1)
    if fare_amount >=8.01 and fare_amount <=12:
        print '%s\t%d' %('8.01,12', 1)
    if fare_amount >=12.01 and fare_amount <=16:
        print '%s\t%d' %('12.01,16', 1)
    if fare_amount >=16.01 and fare_amount <=20:
        print '%s\t%d' %('16.01,20', 1)
    if fare_amount >=20.01 and fare_amount <=24:
        print '%s\t%d' %('20.01,24', 1)
    if fare_amount >=24.01 and fare_amount <=28:
        print '%s\t%d' %('24.01,28', 1)
    if fare_amount >=28.01 and fare_amount <=32:
        print '%s\t%d' %('28.01,32', 1)
    if fare_amount >=32.01 and fare_amount <=36:
        print '%s\t%d' %('32.01,36', 1)
    if fare_amount >=36.01 and fare_amount <=40:
        print '%s\t%d' %('36.01,40', 1)
    if fare_amount >=40.01 and fare_amount <=44:
        print '%s\t%d' %('40.01,44', 1)
    if fare_amount >=44.01 and fare_amount <=48:
        print '%s\t%d' %('44.01,48', 1)
    if fare_amount >=48.01:
        print '%s\t%d' %('48.01,infinite', 1)


