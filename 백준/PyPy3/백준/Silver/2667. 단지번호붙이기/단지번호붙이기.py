import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(10**5)

def dfs(p,q):
    global n
    global count

    if p<0 or p >=n or q < 0 or q >= n:
        return
    if arr[p][q] == 0:
        return
    if [p,q] in visited:
        return

    visited.append([p,q])
    count +=1

    dfs(p-1,q)
    dfs(p + 1, q)
    dfs(p, q-1)
    dfs(p, q+1)


n = int(input())
arr = [[] for i in range(n)]
visited = []

for i in range(n):
    arr[i] = list(input().strip())

tovisit = []
for i in range(n):
    for j in range(n):
        arr[i][j] = int(arr[i][j])
        if arr[i][j] == 1:
            tovisit.append([i,j])

ans = []
for i in tovisit:
    if i not in visited:
        count = 0
        dfs(i[0], i[1])
        ans.append(count)

print(len(ans))
ans.sort()
for i in ans:
    print(i)