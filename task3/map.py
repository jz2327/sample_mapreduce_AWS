#work with Sida Ye
#!/usr/bin/python

import sys
import os
import StringIO
import csv

# input comes from STDIN (stream data that goes to the program)
file_name = os.path.basename(os.environ['mapreduce_map_input_file'])
file_label = file_name[:4]

for line in sys.stdin:
    if file_label == 'task':
        line = line.strip().split('\t')
        line_split_ = line[0].split(',')
        key = key_split_[0]
        value = [file_label] + line_split[1:] + line[1:]
    elif file_label == 'lice':
        csv_file = StringIO.StringIO(line)
        csv_reader = csv.reader(csv_file)
        csv_line = csv_reader.next()
        # skip header
        if csv_line[0] == 'medallion':
            continue
        key = csv_line[0]
        if len(csv_line[1].split(',')) > 1:
            value = [file_label] + ['"{0}"'.format(csv_line[1])] + csv_line[2:]
        else:
            value = [file_label] + csv_line[1:]

    print "{0}\t{1}".format(key, ','.join(value))
