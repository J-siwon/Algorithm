import heapq
import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def dijk(startv):
    d = [1e12 for i in range(n)]
    q = [(0,startv)]
    d[startv] = 0

    while(len(q)>0):
        t = heapq.heappop(q)
        cost = t[0]
        now = t[1]

        if d[now] < cost:
            continue

        for i in arr[now]:
            if d[i[1]] > cost + i[0]:
                d[i[1]] = cost + i[0]
                heapq.heappush(q, (cost + i[0], i[1]))

    return d

n,m,f,s,t = map(int, input().split())

arr = [[] for i in range(n)]
for i in range(m):
    a,b,c = map(int, input().split())
    arr[a].append((c,b))
    arr[b].append((c,a))

d1 = dijk(s)
d2 = dijk(t)
mind = d1[t]
for i in range(f):
    a,b = map(int, input().split())
    mind = min(mind, d1[a]+d2[b])

print(mind)