"""
our teacher has given you the task of drawing a staircase structure. Being an expert programmer, you decided to make a program to draw it for you instead. Given the required height, can you print a staircase as shown in the example?

Input 
You are given an integer NN depicting the height of the staircase.

Output 
Print a staircase of height NN that consists of # symbols and spaces. For example for N=6N=6, here's a staircase of that height:
https://www.hackerrank.com/challenges/staircase
"""
#!/bin/python3

import sys

n = int(input().strip())

for i in range(1, n + 1):
    print((n - i) * " ", end=''),
    print(i * "#") 
