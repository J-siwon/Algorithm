import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n,m = map(int, input().split())
count = [n-1 for i in range(n)]

arr = [[0 for i in range(n)] for i in range(n)]
arr2 = [[0 for i in range(n)] for i in range(n)]
for i in range(m):
    a,b  = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1
    arr2[a - 1][b - 1] = 1
    arr2[b - 1][a - 1] = 1

q = deque()
ans = [0 for i in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            if i !=j:
                count[i] -= 1
                ans[i] +=1
                q.appendleft((i, j, 1))

for i in range(n):
    arr2[i][i] = 1

while(len(q)>0):
    t = q.pop()
    i = t[0]
    j = t[1]
    depth = t[2]+1

    if count[i] == 0:
        continue

    for x in range(n):
        if arr[j][x] == 1 and arr2[i][x] == 0:
            arr2[i][x] = 1
            ans[i] += depth

            q.appendleft((i,x,depth))

for i in range(n):
    if ans[i] == min(ans):
        print(i+1)
        break