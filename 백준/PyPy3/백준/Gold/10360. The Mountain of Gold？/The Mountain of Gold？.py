import heapq
import sys
import math
from collections import deque
input = sys.stdin.readline

times = int(input())
for time in range(1,times+1):
    n,m = map(int, input().split())
    d = [1e9 for i in range(n)]
    d[0] = 0

    e = []
    for i in range(m):
        a,b,c = map(int, input().split())
        e.append((a,b,c))


    ispossible = False
    iscycle = False
    cyclepoint = []
    for i in range(n):
        for j in e:
            if d[j[1]] > d[j[0]] + j[2]:
                d[j[1]] = d[j[0]] + j[2]
                if j[1] == 0:
                    ispossible = True
                    break
                if i == n-1:
                    iscycle = True
                    cyclepoint.append(j[1])
        if ispossible:
            break

    if iscycle:
        d = [1e9 for i in range(n)]
        d[cyclepoint[0]] = 0
        for i in range(n):
            for j in e:
                if d[j[1]] > d[j[0]] + j[2]:
                    d[j[1]] = d[j[0]] + j[2]

        if d[0] < 1e8:
            ispossible = True

    if ispossible:
        print("Case #{0}: possible".format(time))
    else:
        print("Case #{0}: not possible".format(time))