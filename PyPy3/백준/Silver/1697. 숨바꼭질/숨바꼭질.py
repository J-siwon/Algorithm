import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(10**5)

def bfs(p, count):
    global n,m, q
    global isdone
    if visited[p] == True:
        return

    visited[p]= True

    if p == n:
        print(count)
        isdone = True
        return

    count +=1
    if p%2 == 0 and p>n and abs(n-p//2) < abs(n-p):
        tovisit.appendleft([p//2,count])
    else:
        if p < n:
            tovisit.appendleft([p+1,count])
        else:
            tovisit.appendleft([p-1, count])
            tovisit.appendleft([p+1, count])

    while len(tovisit) > 0:
        t= tovisit.pop()
        bfs(t[0], t[1])
        if isdone:
            break


n,m = map(int,(input().split()))
visited = [False for i in range(max(n+1,m*2))]
isdone = False

tovisit = deque()

count = 0
bfs(m,count)
