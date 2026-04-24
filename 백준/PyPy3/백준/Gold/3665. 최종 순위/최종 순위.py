import sys
import math
from collections import deque, Counter

times = int(input())
for time in range(times):
    n = int(input())
    arr = list(map(int, input().split()))
    g = [[] for i in range(n)]

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            g[arr[i]-1].append(arr[j])

    m = int(input())
    iswrong = False
    for i in range(m):
        a,b = map(int, input().split())
        if a in g[b-1]:
            g[b - 1].remove(a)
            g[a - 1].append(b)
        elif b in g[a-1]:
            g[a-1].remove(b)
            g[b-1].append(a)
        else:
            iswrong = True
            break

    if iswrong:
        print("?")
        continue

    c = [0 for i in range(n)]
    for i in range(n):
        for j in g[i]:
            c[j-1] +=1

    q = deque()
    for i in range(len(c)):
        if c[i] == 0:
            q.appendleft(i)

    ans = []
    while(len(q) > 0):
        t = q.pop()
        ans.append(t+1)
        for i in g[t]:
            c[i-1] -=1
            if c[i-1] == 0:
                q.appendleft(i-1)

    for i in c:
        if i !=0:
            iswrong = True
            break

    if iswrong:
        print("IMPOSSIBLE")
    else:
        print(*ans)