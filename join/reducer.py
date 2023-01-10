#!/usr/bin/env python3

import sys
from collections import defaultdict

prev_join_key = None
cur_key_values = defaultdict(list)

for line in sys.stdin:
    try:
        line = line.strip()
        join_key, column = line.split('\t')
        key, value = column.split(':')
    except ValueError:
        continue

    if prev_join_key != join_key:
        if prev_join_key and 'query' in cur_key_values.keys() and 'url' in cur_key_values.keys():
            for query in cur_key_values['query']:
                for url in cur_key_values['url']:
                    print(f'{prev_join_key}\t{query}\t{url}')
        prev_join_key = join_key
        cur_key_values.clear()
    cur_key_values[key].append(value)

if prev_join_key and 'query' in cur_key_values.keys() and 'url' in cur_key_values.keys():
    for query in cur_key_values['query']:
        for url in cur_key_values['url']:
            print(f'{prev_join_key}\t{query}\t{url}')