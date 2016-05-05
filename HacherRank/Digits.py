"""
ven an integer, NN, traverse its digits (dd1,dd2,...,ddn) and determine how many digits evenly divide NN (i.e.: count the number of times NN divided by each digit ddi has a remainder of 00). Print the number of evenly divisible digits.

Note: Each digit is considered to be unique, so each occurrence of the same evenly divisible digit should be counted (i.e.: for N=111N=111, the answer is 33).

Input Format

The first line is an integer, TT, indicating the number of test cases. 
The TT subsequent lines each contain an integer, NN.

Constraints 
1≤T≤151≤T≤15 
0<N<1090<N<109
Output Format

For every test case, count and print (on a new line) the number of digits in NN that are able to evenly divide NN.
"""
#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = raw_input().strip()
    
    count = 0
    for i in n:
        if(i == '0'):
            continue
        if(int(n) % int(i) == 0):
            count += 1
    print count
