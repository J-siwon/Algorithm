import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(10**5)

def bfs(p,q,count):
    global n,m
    global isdone
    if visited[p][q] == True:
        return

    if p == n-1 and q == m-1:
        print(count)
        visited.append([p,q])
        isdone = True
        return

    visited[p][q] = True
    count +=1

    if p >0 and arr[p-1][q] ==1:
        tovisit.appendleft([p - 1,q,count])
    if p < n-1 and arr[p+1][q] ==1:
        tovisit.appendleft([p + 1, q,count])
    if q > 0 and arr[p][q-1] ==1:
        tovisit.appendleft([p, q - 1,count])
    if q < m-1 and arr[p][q+1] ==1:
        tovisit.appendleft([p, q + 1,count])

    while len(tovisit) > 0:
        t= tovisit.pop()
        bfs(t[0], t[1], t[2])
        if isdone:
            break


n,m = map(int,(input().split()))
arr = [[] for i in range(n)]
visited = [[False for i in range(m)] for i in range(n)]
isdone = False

for i in range(n):
    arr[i] = list(input().strip())
    for j in range(len(arr[i])):
        arr[i][j] = int(arr[i][j])


tovisit = deque()

count = 1
bfs(0,0,count)
