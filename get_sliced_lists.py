#!/usr/bin/env python

def get_sliced_lists(n):
    no_last = n[:-1]
    no_first_last = n[1:-1]
    reverse = n[::-1]
    l = [no_last, no_first_last,reverse]

    return l
