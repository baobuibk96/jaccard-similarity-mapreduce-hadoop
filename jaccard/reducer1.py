#!/usr/bin/python3 

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

total_docs = 3
group = ''

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, data = line.split('\t', 1)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += 1
        group += ',' + data
    else:
        if current_word:
            # write result to STDOUT
            if current_count != total_docs and current_count != 1:
                print('%s\t%s' % (current_word, group))

        group = data
        current_count = 1
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    if current_count != total_docs and current_count != 1:
        print('%s\t%s' % (current_word, group))