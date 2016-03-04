​#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    if n == 0:
        print("1")
        continue
        
    feet = 1
    for i in range(1, n + 1):
        if not i % 2 == 0:
            feet *= 2
        else:
            feet += 1
    print(feet)
