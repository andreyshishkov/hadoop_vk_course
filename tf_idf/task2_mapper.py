#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        line = line.strip()
        word, doc, tf = line.split('\t')
    except ValueError:
        continue
    print(f'{word}\t{doc};{tf};1')