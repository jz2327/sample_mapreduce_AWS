#!/usr/bin/python
from operator import itemgetter
import sys

current_key = None
current_total_sum = 0
current_tolls_sum = 0

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    
    key, values = line.strip().split('\t')
    tolls_amount = values.strip().split(',')[1]
    revenue = values.strip().split(',')[0]
    
    try:
        tolls_amount = float(tolls_amount)
        revenue = float(revenue)
    except ValueError:
        continue
    
    if key == current_key:
        current_tolls_sum += tolls_amount
        current_total_sum += revenue
    else:
        if current_key:
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%.2f,%.2f" %(current_key, current_total_sum, current_tolls_sum)
        current_key = key
        current_tolls_sum = tolls_amount
        current_total_sum = revenue

print "%s\t%.2f,%.2f" %(current_key, current_total_sum, current_tolls_sum)