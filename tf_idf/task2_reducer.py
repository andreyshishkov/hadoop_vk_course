#!/usr/bin/env python3

import sys

values = []
prev_word = None
count = 0

for line in sys.stdin:
    try:
        line = line.strip()
        word, value = line.split('\t')
    except ValueError:
        continue

    doc, tf, num = value.split(';')

    if prev_word != word:
        if prev_word:
            for doc_, tf_ in values:
                print(f'{prev_word}#{doc_}\t{tf_}\t{count}')
        prev_word = word
        count = 0
        values.clear()
    count += 1
    values.append((doc, tf))
if prev_word:
    for doc_, tf_ in values:
        print(f'{prev_word}#{doc_}\t{tf_}\t{count}')