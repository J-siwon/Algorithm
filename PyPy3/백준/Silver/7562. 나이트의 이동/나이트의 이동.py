import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(10**5)

def bfs(a,b, count):
    global c,d,n
    global isdone


    if visited[a][b] == True:
        return


    visited[a][b]= True

    if a == c and b == d:
        print(count)
        isdone = True
        return

    count +=1

    if a< n-2 and b< n-1:
        tovisit.appendleft([a+2,b+1,count])
    if a< n-1 and b< n-2:
        tovisit.appendleft([a+1,b+2,count])
    if a> 1 and b< n-1:
        tovisit.appendleft([a-2,b+1,count])
    if a> 0 and b< n-2:
        tovisit.appendleft([a-1,b+2,count])
    if a< n-2 and b > 0:
        tovisit.appendleft([a+2,b-1,count])
    if a< n-1 and b > 2:
        tovisit.appendleft([a+1,b-2,count])
    if a> 1 and b> 0:
        tovisit.appendleft([a-2,b-1,count])
    if a> 0 and b> 1:
        tovisit.appendleft([a-1,b-2,count])

    while len(tovisit) > 0:
        t= tovisit.pop()
        bfs(t[0], t[1],t[2])
        if isdone:
            break


times = int(input())
for time in range(times):
    n = int(input())
    a,b = map(int, input().split())
    c,d = map(int, input().split())
    visited = [[False for _ in range(n)] for _ in range(n)]
    isdone = False

    tovisit = deque()

    count = 0
    bfs(a,b,count)
