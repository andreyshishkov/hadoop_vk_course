#!/usr/bin/env python3

import sys

alpha = 0.1
n = 5

prev_vertex = None
sum_rank = 0
vertexes = set()

for line in sys.stdin:
    try:
        line = line.strip()
        vertex, rank, neighbors = line.split('\t')
    except ValueError:
        continue

    if prev_vertex != vertex:
        if prev_vertex:
            str_vertexes = sorted(list(vertexes), key=lambda x: int(x))
            str_vertexes = '{' + ','.join(str_vertexes) + '}'

            sum_rank = alpha / n + (1 - alpha) * sum_rank

            print(f'{prev_vertex}\t{sum_rank:.3f}\t{str_vertexes}')
        prev_vertex = vertex
        vertexes.clear()
        sum_rank = 0

    if neighbors == '{}':
        sum_rank += float(rank)
    else:
        neighbors = neighbors.strip('{}')
        neighbors = set(neighbors.split(','))
        vertexes = vertexes | neighbors

if prev_vertex:
    str_vertexes = sorted(list(vertexes), key=lambda x: int(x))
    str_vertexes = '{' + ','.join(str_vertexes) + '}'

    sum_rank = alpha / n + (1 - alpha) * sum_rank

    print(f'{prev_vertex}\t{sum_rank:.3f}\t{str_vertexes}')