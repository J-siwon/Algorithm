import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
inf = int(1e9)

def dijk():
    q = []
    heapq.heappush(q, (0,0,0))

    d = [[inf for i in range(c)] for i in range(r)]
    x,y = (0,0)
    while(len(q) > 0):
        t = heapq.heappop(q)
        w = t[0]
        x = t[1]
        y = t[2]

        if d[y][x] < w or (x == c-1 and y == r-1):
            continue

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if tx<0 or tx > c-1 or ty<0 or ty > r-1:
                continue

            if d[ty][tx] > w + arr[ty][tx]:
                d[ty][tx] = w + arr[ty][tx]
                heapq.heappush(q, (w+arr[ty][tx], tx,ty))

    if d[r-1][c-1] > w:
        d[r - 1][c - 1] = w
    print(d[r-1][c-1])


c,r = map(int, input().split())
arr = [[] for i in range(r)]

for i in range(r):
    arr[i] = list(input().strip())
    for j in range(len(arr[i])):
        arr[i][j] = int(arr[i][j])

dijk()