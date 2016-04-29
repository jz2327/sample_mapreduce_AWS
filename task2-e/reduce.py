#!/usr/bin/python
from operator import itemgetter
import sys

current_key = None
count_sum = 0
datetime_list = []
count_date = 0

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    
    key, values = line.strip().split('\t')
    datetime = values.strip().split(',')[0]
    count = values.strip().split(',')[1]
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if key == current_key:
        count_sum += count
        if datetime not in datetime_list:
            datetime_list.append(datetime)
            count_date += 1
    else:
        if current_key:
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%d,%.2f" %(current_key, count_sum, float(count_sum)/count_date)
        current_key = key
        count_sum = count
        datetime_list = [datetime]
        count_date = 1

print "%s\t%d,%.2f" %(current_key, count_sum, float(count_sum)/count_date)
