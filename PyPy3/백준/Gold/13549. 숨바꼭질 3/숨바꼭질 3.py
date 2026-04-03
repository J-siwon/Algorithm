import sys
import math
import heapq
from collections import deque, Counter

a,b = map(int, input().split())
q = [(0,a)]

visited = [1e9 for i in range(2*b+a+1)]
visited[a] = 0
w = 0
while len(q) > 0:
    w, t = heapq.heappop(q)

    if t < b and visited[t+1] > w+1:
        visited[t+1] = w+1
        heapq.heappush(q, (w+1, t + 1))
    if t > 0 and visited[t-1] > w+1:
        visited[t-1] = w+1
        heapq.heappush(q,(w+1, t - 1))
    if t < b and visited[2*t] > w:
        visited[2*t] = w
        heapq.heappush(q,(w, 2 * t))


print(visited[b])