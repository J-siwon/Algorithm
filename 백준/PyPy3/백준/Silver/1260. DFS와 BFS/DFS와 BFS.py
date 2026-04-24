import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(10**5)

def dfs(x):
    global count
    count += 1
    visited[x] = count
    arr[x].sort()
    for i in arr[x]:
        if visited[i] ==0:
            dfs(i)

def bfs(x):
    global count
    count +=1
    visited[x] = count
    arr[x].sort()
    for i in arr[x]:
        if visited[i] == 0:
            visited[i] = count+1
            q.appendleft(i)
    
    if len(q) > 0:
        bfs(q.pop())


n,m,r = map(int,(input().split()))
arr = [[] for i in range(n+1)]
q = deque()
for i in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0 for i in range(n+1)]
count = 0
dfs(r)
for i in range(1,n+1):
    for j in range(1,n+1):
        if visited[j] == i:
            print(j, end= " ")
print()

visited = [0 for i in range(n+1)]
count = 0
bfs(r)
for i in range(1,n+1):
    for j in range(1,n+1):
        if visited[j] == i:
            print(j, end= " ")
