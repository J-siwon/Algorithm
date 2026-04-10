import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
c = []
arr = list(input().split())

for i in arr:
    c.append([i,0])

for i in range(n):
    for j in input().split():
        for k in range(n):
            if c[k][0] == j:
                c[k][1] += 1
                break

c.sort(key = lambda x:(-x[1], x[0]))
for i in c:
    print(i[0], i[1])