"""
Given a square matrix of size N×NN×N, calculate the absolute difference between the sums of its diagonals.

Input Format

The first line contains a single integer, NN. The next NN lines denote the matrix's rows, with each line containing NN space-separated integers describing the columns.

Output Format

Print the absolute difference between the two sums of the matrix's diagonals as a single integer.
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
