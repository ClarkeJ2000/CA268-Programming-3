#!/usr/bin/env python

def get_evenodd_list():
    evens = []
    odds = []
    n = int(input())
    while n != -1:
        if n % 2 != 0:
            odds.append(n)
        else:
            evens.append(n)
        n = int(input())
    return odds,evens
