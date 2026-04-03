import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

maxint = 0
index = arr[0]
c = Counter(arr)
for i in c:
    if c[i] > maxint:
        index = i
        maxint = c[i]
    elif c[i] == maxint:
        index = min(index, i)

print(index)