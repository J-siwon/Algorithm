import heapq
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int, input().split())
arr = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    arr[i] = list(input().strip())
    for j in range(m):
        arr[i][j] = int(arr[i][j])

ans = [[0 for i in range(m)] for i in range(n)]

tovisit = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            tovisit.append((i,j))

qarr = deque()
num = [0 for i in range(len(tovisit))]
iarr = [[0 for i in range(m)] for i in range(n)]
visited = [[0 for i in range(m)] for i in range(n)]
for u in range(len(tovisit)):
    i = tovisit[u][0]
    j = tovisit[u][1]
    if iarr[i][j] != 0:
        continue
    count = 1
    visited[i][j] = 1
    qarr.append((i,j))
    iarr[i][j] = u+1

    while(len(qarr)>0):
        t = qarr.popleft()
        x = t[0]
        y = t[1]
        for q in range(4):
            ni = x + dx[q]
            nj = y + dy[q]
            if ni < 0 or ni > n - 1 or nj < 0 or nj > m - 1 or arr[ni][nj] != 0:
                continue
            if visited[ni][nj] == 0:
                visited[ni][nj] = 1
                iarr[ni][nj] = u+1
                count+=1
                qarr.append((ni,nj))

    num[u] = count

for i in range(n):
    for j in range(m):
        visited = []
        if arr[i][j] == 1:
            ans[i][j] = 1
            for q in range(4):
                ni = i + dx[q]
                nj = j + dy[q]
                if ni < 0 or ni > n - 1 or nj < 0 or nj > m - 1 or arr[ni][nj] != 0:
                    continue

                if iarr[ni][nj] not in visited:
                    visited.append(iarr[ni][nj])
                    ans[i][j] += num[iarr[ni][nj]-1]
                    ans[i][j] %= 10

for i in range(n):
    for j in range(m):
        print(ans[i][j], end = "")
    print()