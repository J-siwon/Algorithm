import sys
import math
from collections import deque, Counter
input = sys.stdin.readline


arr = []
for i in range(1,10001):
    t = 0
    x = i
    t += x
    if i >= 1000:
        t += x//1000
        x = x %1000
        
    if i >= 100:
        t += x//100
        x = x %100
    
    if i >= 10:
        t += x//10
        x = x %10    

    t += x
    if i != t:
        arr.append(t)

for i in range(1, 10001):
    if i not in arr:
        print(i)