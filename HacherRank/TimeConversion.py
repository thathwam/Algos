"""
https://www.hackerrank.com/challenges/time-conversion
"""

import sys

time = input().strip()

hourStr, minStr, secStr = time.split(":")
if "AM" in time and hourStr == "12":
    hourStr = "00"
elif "PM" in time and hourStr != "12":
    hourStr = str(int(hourStr) + 12)
    
print(hourStr + ":" + minStr + ":" + secStr[0:2])
