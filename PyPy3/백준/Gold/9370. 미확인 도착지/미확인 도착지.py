import sys
import math
import heapq
from collections import deque, Counter

def dijk(startv):
    d = [1e9 for i in range(n)]

    q = [(0,startv)]
    d[startv-1] = 0
    while len(q) > 0:
        t = heapq.heappop(q)
        a = t[0]
        b = t[1]
        for i in arr[b - 1]:
            if d[i[0] - 1] > a + i[1]:
                d[i[0] - 1] = a+i[1]
                heapq.heappush(q, (a + i[1], i[0]))

    return d


times = int(input())
for time in range(times):
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())

    sgw = 0
    arr = [[] for _ in range(n)]
    for i in range(m):
        a,b,d = map(int, input().split())
        arr[a-1].append([b,d])
        arr[b-1].append([a,d])
        if (a==g and b==h) or (a==h and b==g):
            sgw = d

    dest = []
    for i in range(t):
        dest.append(int(input()))

    d = dijk(s)
    d1 = dijk(h)
    d2 = dijk(g)
    t1 = d[g-1] + sgw
    t2 = d[h-1] + sgw

    dest = sorted(dest)
    for i in dest:
        if d[i-1] == min(d1[i-1]+t1, d2[i-1]+t2):
            print(i, end = " ")
    print()