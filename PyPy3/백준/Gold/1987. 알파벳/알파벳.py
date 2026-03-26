import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

def dfs(x,y,visited):
    global maxlen
    maxlen = max(maxlen, len(visited))
    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]
        if nr < 0 or nc < 0 or nr > r-1 or nc > c-1:
            continue

        if arr[nr][nc] in visited:
            continue
        dfs(nr,nc,visited + arr[nr][nc])

dr = [1,-1,0,0]
dc = [0,0,1,-1]

r,c = map(int, input().split())
arr = [[] for i in range(r)]
for i in range(r):
    arr[i] = list(input().strip())

maxlen = 1
dfs(0,0,arr[0][0])
print(maxlen)