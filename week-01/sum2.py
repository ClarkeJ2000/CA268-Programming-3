#!/usr/bin/env python

i = 0
for i in range(len(lst)):
    j = i
    for j in range(len(lst)):
        if lst[i] + lst[j] == k:
            print(lst[i], lst[j])
