import sys
import math
import heapq
from collections import deque, Counter

times = int(input())
n = int(input())
arr = [[] for i in range(4)]
p = [25 for i in range(4)]

for i in range(n):
    a,b,c = input().split()
    arr[ord(a)- ord("A")].append((ord(b)-ord("A"),c))


for time in range(times):
    t = [0 for i in range(4)]
    for i in range(4):
        for j in arr[i]:
            (a,b) = j
            t[a] += float(b)*p[i]
    p = t.copy()
for i in p:
    print(i)