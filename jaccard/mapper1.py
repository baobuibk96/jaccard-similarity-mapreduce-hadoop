#! /usr/bin/python3  


import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    id, text = line.split(' ', 1)

    # split the line into words
    words = text.split()

    # increase counters
    W = 0
    q = {}
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if word not in q:
            q[word] = 1
            W += 1

    for key in q:
        print('%s\t%s@%s' % (key, id, W))
        
    