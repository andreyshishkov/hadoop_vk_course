#!/usr/bin/env python3

import sys

prev_vertex = None
min_dist = float('+inf')
vertexes = set()

for line in sys.stdin:
    try:
        line = line.strip()
        vertex, dist, neighbors = line.split('\t')
    except ValueError:
        continue

    dist = float('+inf') if dist == 'INF' else int(dist)
    neighbors = neighbors.strip('{}').split(',') if neighbors != '{}' else []
    neighbors = set(neighbors)

    if vertex != prev_vertex:
        if prev_vertex:
            vertexes = sorted(list(vertexes), key=lambda x: int(x))
            str_vertexes = '{' + ','.join(vertexes) + '}' if vertexes else '{}'
            min_dist = 'INF' if min_dist == float('+inf') else min_dist
            print(f'{prev_vertex}\t{min_dist}\t{str_vertexes}')
        min_dist = float('+inf')
        vertexes = set()
        prev_vertex = vertex
    min_dist = min(min_dist, dist)
    vertexes = vertexes | neighbors

if prev_vertex:
    vertexes = list(vertexes)
    str_vertexes = '{' + ','.join(vertexes) + '}' if vertexes else '{}'
    min_dist = 'INF' if min_dist == float('+inf') else min_dist
    print(f'{prev_vertex}\t{min_dist}\t{str_vertexes}')