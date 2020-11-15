#!/usr/bin/env python

print("Enter a name and number, or a name and ? to query (!! to exit)")
n = input()
d = {}
while n != '!!':
    n = n.split(' ')
    if n[1] == '?':
        if n[0] in d.keys():
            print(str(n[0]) + ' has number ' + str(d[n[0]]))
        else:
            print('Sorry, there is no ' + str(n[0]))
    else:
        d[n[0]] = n[1]
    n = input()
if n == '!!':
    print('Bye')

