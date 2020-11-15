#!/usr/bin/env python3

def make_map():
    n = input()
    students = {}
    while n != '' :
        x = n.split(' ')
        students[x[0]] = x[1]
        n = input()
    return students
