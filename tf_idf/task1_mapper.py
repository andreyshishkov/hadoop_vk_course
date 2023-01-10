#!/usr/bin/env python3

import sys
import re

pattern = re.compile('\w+')

for line in sys.stdin:
    line = line.strip()
    doc_num, doc = line.split(':', 1)

    words = pattern.findall(doc)
    for word in words:
        print(f'{word}#{doc_num}\t1')