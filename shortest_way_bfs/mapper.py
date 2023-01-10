#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        line = line.strip()
        vertex, dist, adj_list = line.split('\t')
    except ValueError:
        continue
    print(line)

    dist = int(dist) + 1 if dist != 'INF' else dist
    neighbors = adj_list.strip('{}').split(',')
    if neighbors == ['']:
        continue
    for neighbor in neighbors:
        print(f'{neighbor}\t{dist}\t' + '{}')
