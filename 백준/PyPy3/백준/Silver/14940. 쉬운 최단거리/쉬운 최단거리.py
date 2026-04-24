import heapq
import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int, input().split())
arr = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

ans = [[1e9 for i in range(m)] for i in range(n)]

startx = -1
starty = -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            startx = i
            starty = j
            break
    if startx != -1:
        break

qarr = deque([(startx, starty, 0)])
while(len(qarr)>0):
    t = qarr.popleft()
    i = t[0]
    j = t[1]
    if ans[i][j] <= t[2]:
        continue
    ans[i][j] = t[2]
    for q in range(4):
        ni = i + dx[q]
        nj = j + dy[q]
        if ni < 0 or ni > n - 1 or nj < 0 or nj > m - 1:
            continue

        if arr[ni][nj] == 0:
            ans[ni][nj] = 0
            continue
        if ans[ni][nj] > t[2] + 1:
            qarr.append((ni,nj,t[2]+1))

for i in range(n):
    for j in range(m):
        if ans[i][j] > 1e8:
            if arr[i][j] == 0:
                ans[i][j] = 0
            else:
                ans[i][j] = -1

arr[startx][starty] = 0
for i in range(n):
    print(*ans[i])