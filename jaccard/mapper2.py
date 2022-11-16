#! /usr/bin/python3  


import sys

count = {}
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, data = line.split('\t', 1)

    # split the line into words
    docs = data.split(',')

    for doc in docs:
        for doc2 in docs:
            key = doc + ',' + doc2
            key2 = doc2 + ',' + doc
            if doc != doc2 and key2 not in count:
                 print('%s,%s\t%s' % (doc, doc2, 1))
        
    