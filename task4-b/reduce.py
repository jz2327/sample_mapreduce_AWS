#!/usr/bin/python
from operator import itemgetter
import sys

current_key = None
total_amount_sum = 0
agent_dict = {}

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
    
    key, total_amount = line.strip().split('\t')

    try:
        total_amount = float(total_amount)
    except ValueError:
        continue
    
    if key == current_key:

        total_amount_sum += total_amount

    else:
        if current_key:
            # output goes to STDOUT (stream data that the program writes)
            agent_dict[current_key] = total_amount_sum

        current_key = key
        total_amount_sum = total_amount

agent_dict[current_key] = total_amount_sum

sorted_agent = sorted(agent_dict.items(), key=itemgetter(1))

for i in range(20):
    print '%s\t%.2f' %(sorted_agent[i][0], sorted_agent[i][1])

