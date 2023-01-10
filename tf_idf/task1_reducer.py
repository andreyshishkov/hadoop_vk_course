#!/usr/bin/env python3
import sys

prev_key = None
count = 0

for line  in sys.stdin:
    try:
        line = line.strip()
        key, cur_count = line.split('\t')
    except ValueError:
        continue
    if prev_key != key:
        if prev_key:
            word, doc = prev_key.split('#')
            print(f'{word}\t{doc}\t{count}')
        prev_key = key
        count = 0
    count += 1
if prev_key:
    word, doc = prev_key.split('#')
    print(f'{word}\t{doc}\t{count}')