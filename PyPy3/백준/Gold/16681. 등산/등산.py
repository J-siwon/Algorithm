import heapq
import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

INF = int(1e12)
def dijk(startv):
    d = [INF for i in range(n)]
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
            if d[i[1]-1] > cost + i[0]:
                d[i[1]-1] = cost + i[0]
                heapq.heappush(q,(cost+i[0], i[1]))

    return d

n,m,d,e = map(int,input().split())
h = list(map(int,input().split()))

arr = [[]for i in range(n)] #올라가기
for i in range(m):
    a,b,c = map(int, input().split())
    if h[a-1] < h[b-1]:
        arr[a-1].append((c*d, b))
    elif h[a-1] > h[b-1]:
        arr[b - 1].append((c * d, a))


d = dijk(1)
d2 = dijk(n) #n에서부터 올라가는 거리 = i번에서 n까지 내려가는 거리
ans = -1e12
isdone = False
for i in range(len(d)):
    if i == 0 or i == n-1 or d[i] == INF or d2[i] == INF:
        continue
    ans = max(ans, -d[i] + -d2[i] + h[i]*e)
    isdone = True

if isdone:
    print(ans)
else:
    print("Impossible")

