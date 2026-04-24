import sys
import math
import heapq
from collections import deque, Counter

def dijkstra(a,b):
    global v
    q = [(0,a)]
    d = [1e9 for i in range(v)]
    isf = False
    fw = 0
    while len(q)>0:
        w,t = heapq.heappop(q)

        if d[t-1] < w:
            continue

        d[t-1] = w

        for i in arr[t-1]:
            if d[i[0]-1] > w + i[1]:
                heapq.heappush(q, (w+i[1], i[0]))

    return d[b-1]


v,e = map(int, input().split())
arr = [[] for i in range(v)]
for i in range(e):
    a,b,w = map(int, input().split())
    arr[a-1].append((b,w))
    arr[b-1].append((a,w))

f1, f2 = map(int, input().split())

startv = 1

t1 = (dijkstra(startv, f1) + dijkstra(f1,f2) + dijkstra(f2,v))
t2 = (dijkstra(startv, f2) + dijkstra(f2,f1) + dijkstra(f1,v))
ans = min(t1,t2)
if ans > 1e7:
    print(-1)
else:
    print(ans)