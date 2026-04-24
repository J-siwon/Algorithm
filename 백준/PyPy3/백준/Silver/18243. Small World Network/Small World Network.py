import heapq
import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def dijk(startv):
    d = [1e9 for i in range(n)]
    d[startv-1] = 0

    q = []
    heapq.heappush(q, (0,startv))
    while(len(q) > 0):
        t = heapq.heappop(q)
        cost = t[0]
        now = t[1]

        if d[now-1] < cost:
            continue

        for i in arr[now-1]:
            if d[i-1] > cost + 1:
                d[i-1] = cost+1
                q.append((cost+1, i))

    return d

n,m = map(int, input().split())
arr = [[] for i in range(n)]
for i in range(m):
    a,b= map(int, input().split())
    arr[a-1].append(b)
    arr[b-1].append(a)

isbig = False
for i in range(1,n+1):
    for j in dijk(i):
        if j > 6:
            isbig = True
            break
    if isbig:
        break

if isbig:
    print("Big World!")
else:
    print("Small World!")