#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        line = line.strip()
        num, groups = line.split('\t', 1)
    except ValueError:
        continue

    groups = groups.split(',')
    for group in groups:
        print(f'{num},{group}\t1')