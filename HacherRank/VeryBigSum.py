"""
You are given an array of integers of size NN. You need to print the sum of the elements in the array, keeping in mind that some of those integers may be quite large.

Input

The first line of the input consists of an integer NN. The next line contains NN space-separated integers contained in the array.

Constraints 
1≤N≤101≤N≤10 
0≤A[i]≤10100≤A[i]≤1010

Sample Input 
5
1000000001 1000000002 1000000003 1000000004 1000000005

Output 
Print a single value eq
"""

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print(sum(arr))
