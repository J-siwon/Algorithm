import heapq
import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

INF = int(1e12)
n,startv,endv,m = map(int,input().split())

e = []
for i in range(m):
    a,b,c = map(int, input().split())
    e.append((a,b,c))

value = list(map(int,input().split()))
for i in range(len(e)):
    e[i] = (e[i][0], e[i][1], e[i][2] - value[e[i][1]])

iscycle = False
d = [INF for i in range(n)]
d[startv] = 0
cyclepoint = []
for i in range(n):
    for j in e:
        if d[j[0]] != INF and d[j[1]] > d[j[0]] + j[2]:
            d[j[1]] = d[j[0]] + j[2]
            if i == n-1:
                iscycle = True
                cyclepoint.append(j[0])

if d[endv] == INF:
    print("gg")
else:
    if iscycle:
        isjoined = False
        for k in cyclepoint:
            d2 = [INF for i in range(n)]
            d2[k] = 0
            for i in range(n):
                for j in e:
                    if d2[j[0]] != INF and d2[j[1]] > d2[j[0]] + j[2]:
                        d2[j[1]] = d2[j[0]] + j[2]
            if d2[endv] != INF:
                isjoined = True

        if not isjoined:
            print(-d[endv] + value[startv])
        else:
            print("Gee")
    else:
        print(-d[endv] + value[startv])