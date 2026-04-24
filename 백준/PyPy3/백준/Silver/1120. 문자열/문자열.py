import sys
import math
import heapq
from collections import deque, Counter

a,b = input().split()
c = 0
minc =1e9
t = 0
for i in range(len(b)-len(a)+1):
    x = b[i:]
    c = 0
    for j in range(len(a)):
        if a[j] != x[j]:
            c += 1

    minc = min(c, minc)
    t +=1

print(minc)