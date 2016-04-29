#!/usr/bin/python

import sys
import pandas as pd

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    line_str = line.strip()
    lines = line_str.split(',')

    # skip header
    if lines[0] == 'VendorID':
        continue

    weekday = pd.to_datetime(lines[1]).weekday()

    line_to_delete = [0,7,8,11,13,14,16,17]

    for variable in line_to_delete: 
        del lines[variable]

    print '%s\t%s' %(weekday, lines)



