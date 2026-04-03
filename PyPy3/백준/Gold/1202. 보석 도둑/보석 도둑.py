import sys
import math
import heapq
from collections import deque, Counter

n,m = map(int, input().split())

q = []
for i in range(n):
    w,v = map(int, input().split())
    heapq.heappush(q,(w,-v))

blist = []
for i in range(m):
    b = int(input())
    blist.append(b)

blist = sorted(blist, reverse= True)
c = 0

t = []
while(len(blist) > 0):
    b = blist.pop()
    w = 0
    while(w <= b and len(q)>0):
        w,v = heapq.heappop(q)
        v = -v
        if w > b:
            heapq.heappush(q,(w,-v))
            break
        heapq.heappush(t, -v)

    if len(t)>0:
        c += -heapq.heappop(t)
print(c)