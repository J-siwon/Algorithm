import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(10**5)

def dfs(x, cyclecount):
    global iscycle

    if flag[x] != 0:
        if (cyclecount - flag[x]) % 2 ==0:
            iscycle = True
        return
    
    cyclecount +=1
    flag[x] = cyclecount
    for i in arr[x]:
        dfs(i, cyclecount)


times = int(input())
for time in range(times):
    v,e = map(int, input().split())
    arr = [[] for i in range(v+1)]

    for i in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    flag = [0 for i in range(v+1)]
    cyclecount = 0
    iscycle = False
    for i in range(1,v+1):
        if flag[i] != 0:
            continue
        dfs(i, cyclecount)
        
        if iscycle:
            break
        
    if iscycle:
        print("NO")
    else:
        print("YES")