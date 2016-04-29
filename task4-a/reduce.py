#!/usr/bin/python
from operator import itemgetter
import sys

current_key = None
current_sum = 0
total_amount_sum = 0
tips_amount_sum = 0

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    
    key, line_strip = line.strip().split('\t')
    total_amount = line_strip.split(',')[0]
    tips_percentage = line_strip.split(',')[1]
    count = line_strip.split(',')[2]

    try:
        count = int(count)
        total_amount = float(total_amount)
        tips_percentage = float(tips_percentage)
    except ValueError:
        continue
    
    if key == current_key:
        current_sum += count
        total_amount_sum += total_amount
        tips_amount_sum += tips_percentage

    else:
        if current_key:
            # output goes to STDOUT (stream data that the program writes)
            if total_amount_sum == 0:
                print "%s\t%d,%.2f,%.2f" %(current_key, current_sum, 0, 0)
            else:
                print "%s\t%d,%.2f,%.2f" %(current_key, current_sum, total_amount_sum, tips_amount_sum/current_sum*100)
        
        current_key = key
        current_sum = count
        total_amount_sum = total_amount
        tips_amount_sum = tips_percentage

if total_amount_sum == 0:
    print "%s\t%d,%.2f,%.2f" %(current_key, current_sum, 0, 0)
else:
    print "%s\t%d,%.2f,%.2f" %(current_key, current_sum, total_amount_sum, tips_amount_sum/current_sum*100)

