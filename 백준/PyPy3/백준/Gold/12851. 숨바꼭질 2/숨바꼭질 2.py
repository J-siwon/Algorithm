import sys
import math
from collections import deque, Counter

n,m = map(int, input().split())
visited = [0 for i in range(2*m+n+1)]
q = deque()
nc = 0
q.appendleft([n,0])
c = 0
isdone = False
while(len(q) > 0):
    t = q.pop()
    nt = t[0]

    if isdone and nc != t[1]+1:
        break

    nc = t[1]
    if nt == m:
        break
    visited[nt] = nc
    nc += 1

    if nt > 0 and visited[nt-1] == 0 :
        if nt - 1 == m:
            c += 1
            isdone = True
        q.appendleft([nt - 1,nc])
    if nt <m and visited[nt+1] == 0:
        if nt + 1 == m :
            c += 1
            isdone = True
        q.appendleft([nt + 1, nc])
    if  nt < m and visited[nt*2] == 0:
        if nt * 2 == m:
            c += 1
            isdone = True
        q.appendleft([2 * nt,nc])

print(nc)
if c == 0:
    c = 1
print(c)