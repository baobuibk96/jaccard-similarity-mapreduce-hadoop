#! /usr/bin/python3  


import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, data = line.split('\t', 1)

    # split the line into words
    docs = data.split(',')

    count = {}
    for doc in docs:
        for doc2 in docs:
            if doc != doc2:
                list = [doc, doc2]
                list.sort()
                key = ','.join(list)
                if key not in count:
                    count[key] = 1
                    print('%s\t%s' % (key, 1))
        
    