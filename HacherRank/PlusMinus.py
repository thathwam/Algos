"""
https://www.hackerrank.com/challenges/plus-minus
"""
#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

minus = 0
plus = 0 
zero = 0

for item in arr:
    if item < 0:
        minus += 1
    elif item > 0:
        plus += 1
    else:
        zero += 1
        
print(plus / n)
print(minus / n)
print(zero / n)
