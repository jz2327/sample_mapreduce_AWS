#work with Sida Ye
#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
current_key = None
current_dict = {}

for line in sys.stdin:

    key, value = line.strip().split("\t")
    value = value.split(',')
    file_label = value[0]

    if key == current_key:
        if file_label not in current_dict:
            current_dict[file_label] = [value[1:]]
        else:
            current_dict[file_label].append(value[1:])

    else:
        if current_key:
            if ('task' in current_dict) and ('lice' in current_dict):
                for t in current_dict['task']:
                    for f in current_dict['lice']:
                        v = ','.join(t) + ',' + ','.join(f)
                        print "{0}\t{1}".format(current_key, v)
        current_key = key
        current_dict = {file_type: [value[1:]]}

if ('task' in current_dict) and ('lice' in current_dict):
    for t in current_dict['task']:
        for f in current_dict['lice']:
            v = ','.join(t) + ',' + ','.join(f)
            print "{0}\t{1}".format(current_key, v)
