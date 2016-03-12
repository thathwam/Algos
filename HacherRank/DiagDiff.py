"""
Find the diagonal diff in a matrix
https://www.hackerrank.com/challenges/diagonal-difference
"""

#!/bin/python3

import sys

n = int(input().strip())
a = []
for a_i in range(n):
   a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
   a.append(a_t)

leftSum = 0
rightSum = 0

for i, list in enumerate(a):
    leftSum += list[i]
#print(leftSum)

for i, list in enumerate(a):
    rightSum += list[n - i - 1]
#print(rightSum)

print(abs(leftSum - rightSum))
