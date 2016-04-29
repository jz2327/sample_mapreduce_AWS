#!/usr/bin/python
from operator import itemgetter
import sys

current_sum = 0

# input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:

    current_sum += 1

print '%d' %(current_sum)

