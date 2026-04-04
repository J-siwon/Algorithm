import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

s = []
for i in range(int(input())):
    s.append(input().strip())

c = Counter(s)

maxc = 0
maxi = 0
for i in c:
    if c[i] > maxc:
        maxc = c[i]
        maxi = i
    elif c[i] == maxc:
        t = []
        t.append(maxi)
        t.append(i)
        t.sort()
        maxi = t[0]

print(maxi)