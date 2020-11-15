#!/usr/bin/env python

def get_plural(word):
    if word[:-2] == 'ch' or 'sh':
        word = word + 'es'
    elif word[:-1] == 'y':
        word = word + 'ies'
    elif word[:-1] == 'f':
        word = word + 'ves'
    elif word[:-1] == 'fe':
        word = word + 'ves'
    elif word[:-1] == 'o' or 'x' or 's' or 'z':
        word = word + 'es'
    else:
        word = word + 's'