#!/usr/bin/python
from operator import itemgetter
import sys

current_key = None
count_sum = 0
medallion = []

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    
    key, medallion = line.strip().split('\t')
    
    if key == current_key:
        if medallion not in medallion_list:
            medallion_list.append(medallion)
            count_sum += 1
    else:
        if current_key:
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%d" %(current_key, count_sum)
        current_key = key
        count_sum = 1
        medallion_list = [medallion]

print "%s\t%d" %(current_key, count_sum)