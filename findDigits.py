
"""https://www.hackerrank.com/challenges/find-digits"""

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
