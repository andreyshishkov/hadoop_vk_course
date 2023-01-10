#!/usr/bin/env python3
import sys
from collections import defaultdict

counter = defaultdict(int)  # count category
prev_value = None
tmp_set = set()

for line in sys.stdin:
    try:
        line = line.strip()
        value, category = line.split('\t')
    except ValueError:
        continue

    if value != prev_value:
        if prev_value:
            for cat in tmp_set:
                counter[cat] += 1
        prev_value = value
        tmp_set = {category}
    else:
        tmp_set.add(category)

if prev_value:
    for cat in tmp_set:
        counter[cat] += 1

for key, count in counter.items():
    print(f'{key}\t{count}')