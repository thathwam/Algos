"""
Given an array of integers, calculate which fraction of the elements are positive, negative, and zeroes, respectively. Print the decimal value of each fraction.

Input Format

The first line, NN, is the size of the array. 
The second line contains NN space-separated integers describing the array of numbers (A1,A2,A3,⋯,ANA1,A2,A3,⋯,AN).

Output Format

Print each value on its own line with the fraction of positive numbers first, negative numbers second, and zeroes third.

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
