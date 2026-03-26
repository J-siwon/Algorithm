import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

INF = int(1e12)

def dijk(kmax):
    d = [[INF for i in range(n)] for i in range(kmax+1)]
    for i in range(kmax):
        d[i][0] = 0
    parent[0] = 1
    deletable = kmax

    q = [(0,1,deletable)]
    while(len(q)>0):
        t = heapq.heappop(q)
        now = t[1]
        cost = t[0]
        if d[t[2]][now-1] < cost or now == n:
            continue

        for i in arr[now-1]:
            if d[t[2]][i[1]-1] > cost + i[0]:
                d[t[2]][i[1]-1] = cost + i[0]
                heapq.heappush(q, (cost+i[0], i[1], t[2]))
                parent[i[1]-1] = now
            deletable = t[2] - 1
            if deletable >= 0 and d[deletable][i[1]-1] > cost:
                d[deletable][i[1] - 1] = cost
                heapq.heappush(q, (cost, i[1], deletable))

    mincost = INF
    for i in range(kmax):
        mincost = min(d[i][n-1], mincost)
    return mincost

n,m,k = map(int, input().split())
arr = [[] for i in range(n)]
indegree = [[] for i in range(n)]
for i in range(m):
    a,b,c = map(int, input().split())
    arr[a-1].append((c,b))
    arr[b-1].append((c,a))

parent = [INF for i in range(n)]

mincost = INF

d = dijk(k)

print(d)