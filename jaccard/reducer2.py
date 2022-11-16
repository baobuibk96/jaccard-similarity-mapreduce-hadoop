#!/usr/bin/python3  


from operator import itemgetter
import sys

current_data = None
current_count = 0
data = None

total_docs = 87

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    data, value = line.split('\t', 1)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: data) before it is passed to the reducer
    if current_data == data:
        current_count += 1
    else:
        if current_data:
            doc1, doc2 = current_data.split(',', 1)
            id1, w1 = doc1.split('@', 1)
            id2, w2 = doc2.split('@', 1)
            w1 = int(w1)
            w2 = int(w2)
            print('%s\t%s\t%s' % (id1, id2, current_count / (w1 + w2 - current_count)))

        current_count = 1
        current_data = data

# do not forget to output the last data if needed!
if current_data == data:
    doc1, doc2 = current_data.split(',', 1)
    id1, w1 = doc1.split('@', 1)
    id2, w2 = doc2.split('@', 1)
    w1 = int(w1)
    w2 = int(w2)
    print('%s\t%s\t%s' % (id1, id2, current_count / (w1 + w2 - current_count)))