#!/usr/bin/env python3

def get_odd_list():
    n = int(input())
    l = []
    while n != -1:
        if n % 2 == 1:
            l.append(n)
        n = int(input())
    return l
