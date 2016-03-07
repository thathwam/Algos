#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    
    inTime = 0
    for std in a:
        if std <= 0:
            inTime += 1
    if inTime < k:
        print("YES")
    else:
        print("NO")




