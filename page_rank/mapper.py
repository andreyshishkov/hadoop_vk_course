#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        line = line.strip()
        vertex, rank, neighbors = line.split('\t')
    except ValueError:
        continue

    rank = float(rank)
    neighbors = neighbors.strip('{}').split(',')
    neighbors = neighbors if neighbors != [''] else []

    print(line)
    sended_rank = rank / len(neighbors)
    for neighbor in neighbors:
        print(f'{neighbor}\t{sended_rank:.3f}\t' + '{}')