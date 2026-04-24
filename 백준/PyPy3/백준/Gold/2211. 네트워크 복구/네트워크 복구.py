import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

def dijk(startv, endv):
    d = [1e9 for i in range(n)]
    d[startv-1] = 0
    q = []

    heapq.heappush(q, (0,startv, 1))

    while(len(q)>0):
        t = heapq.heappop(q)
        now = t[1]
        cost = t[0]
        count = t[2]

        if cost > d[now-1]:
            continue

        for i in arr[now-1]:
            if d[i[1]-1] == cost + i[0] and visited[i[1]-1][1] > count:
                visited[i[1]-1] = (now,count)

            if d[i[1]-1] > cost + i[0]:
                d[i[1]-1] = cost + i[0]
                heapq.heappush(q, (cost + i[0], i[1], count + 1))
                visited[i[1]-1] = (now,count)

    return d


n,m = map(int, input().split())
arr = [[]for i in range(n)]
visited = [(0,1e9) for i in range(n)]
for i in range(m):
    a,b,c = map(int, input().split())
    arr[a-1].append((c,b))
    arr[b-1].append((c,a))

dijk(1, 0)

ans = set()
for i in range(1,n):
    t = visited[i][0]
    ans.add((i+1,t))

print(len(ans))
for i in ans:
    print(*i)