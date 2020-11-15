#!/usr/bin/env python

def get_counts(words):
    count = [0] * 10
    l = 0

    for i in word:
        if len(i) <= 9:
            l = len(i)
            x = int(count[l])
            count[l] = x + 1

        return count
