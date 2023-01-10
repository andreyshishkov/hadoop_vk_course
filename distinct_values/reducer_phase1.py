# /usr/bin/env python3

import sys

prev_key = None

for line in sys.stdin:
    try:
        line = line.strip()
        key, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue

    if key != prev_key:
        if prev_key:
            print(prev_key)
        prev_key = key

if prev_key:
    print(prev_key)