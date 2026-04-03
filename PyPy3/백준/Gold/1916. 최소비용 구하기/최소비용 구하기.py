import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for i in range(n)]
for i in range(m):
    a,b,w = map(int, input().split())
    arr[a-1].append((w,b))

start, end = map(int, input().split())
d = [1e9 for i in range(n)]
q = []
for i in arr[start-1]:
    heapq.heappush(q,i)
    d[i[1]-1] = min(d[i[1]-1],i[0])
d[start-1] = 0

while len(q) > 0:
    t = heapq.heappop(q)
    w = t[0]
    a = t[1]

    if d[a-1] < w:
        continue

    for i in arr[a-1]:
        if d[i[1]-1]  > w + i[0]:
            d[i[1]-1] = w + i[0]
            heapq.heappush(q, (w + i[0], i[1]))

print(d[end-1])