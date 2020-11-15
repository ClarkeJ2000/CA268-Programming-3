#!/usr/bin/env python

import sys
from Stack import Stack

def reverse_input(stack):
    n = input()
    while n != 'line3':
        stack.push(n)
        n = input()

    stack.push('line3')

    while not stack.is_empty():
        print(stack.pop())
