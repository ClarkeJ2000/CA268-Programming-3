#!/usr/bin/env python

import sys

file = sys.argv[1]
i = 0
while i < len(file):
    print(file[i:i + 2])
    i += 1