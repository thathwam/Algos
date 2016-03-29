
"""
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. How tall will her tree be after NN growth cycles?

Input Format

The first line contains an integer, TT, the number of test cases. 
TT subsequent lines each contain an integer, NN, denoting the number of cycles for that test case.

Constraints 
1≤T≤101≤T≤10 
0≤N≤600≤N≤60
Output Format

For each test case, print the height of the Utopian Tree after NN cycles. Each height must be printed on a new line.

https://www.hackerrank.com/challenges/utopian-tree
​#!/bin/python3
"""
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
