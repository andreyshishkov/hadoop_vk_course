#!/usr/bin/env python3
import sys

prev_word = None
count = 0

for line in sys.stdin:
    line = line.strip()
    try:
        word, cur_count = line.split('\t')
        cur_count = int(cur_count)
        if prev_word is None:
            prev_word = word
        if word == prev_word:
            count += cur_count
        else:
            print(f'{prev_word}\t{count}')
            count = 1
            prev_word = word
    except ValueError:
        continue
print(f'{prev_word}\t{count}')