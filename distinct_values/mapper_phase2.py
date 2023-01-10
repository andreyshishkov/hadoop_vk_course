#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        line = line.strip()
        key, value = line.split(',', 1)
    except ValueError:
        continue

    print(f'{value}\t{1}')