import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

def dijk(startv):
    d= [1e9 for i in range(n)]
    d[startv-1] = 0

    q = []
    heapq.heappush(q,(0,startv))

    while(len(q) > 0):
        t = heapq.heappop(q)
        cost = t[0]
        dest = t[1]
        if d[dest-1] < cost:
            continue

        for i in arr[dest-1]:
            if d[i[1]-1] > cost + i[0]:
                d[i[1] - 1] = cost + i[0]
                heapq.heappush(q, (cost + i[0], i[1]))

    return d

#N명의 학생 X번 파티 M개 단방향 도로

n,m,x = map(int, input().split())
arr =[[] for i in range(n)]
for i in range(m):
    a,b,c = map(int, input().split())
    arr[a-1].append((c,b))

ans = 0
for i in range(n):
    ans = max(ans, dijk(i+1)[x-1] + dijk(x)[i])

print(ans)