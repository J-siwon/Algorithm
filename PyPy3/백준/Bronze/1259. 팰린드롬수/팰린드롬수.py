import sys
import math
from collections import deque, Counter

s = input().strip()
while(int(s) != 0):
    if s == s[::-1]:
        print("yes")
    else:
        print("no")
    s = input().strip()