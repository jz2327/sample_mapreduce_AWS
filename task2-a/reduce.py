#!/usr/bin/python
from operator import itemgetter
import sys

current_key = None
current_sum = 0

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    
    key, count = line.strip().split('\t', 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if key == current_key:
        current_sum += count
    else:
        if current_key:
            # output goes to STDOUT (stream data that the program writes)
            print "%s\t%d" %(current_key, current_sum)
        current_key = key
        current_sum = count

print "%s\t%d" %(current_key, current_sum)