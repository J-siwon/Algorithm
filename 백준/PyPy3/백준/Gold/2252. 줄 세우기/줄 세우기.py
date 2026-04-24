import sys
import math
from collections import deque, Counter

n,m = map(int, input().split())
arr = [[] for i in range(n+1)]
c = [0 for i in range(n+1)]
q = deque()
for i in range(m):
    a,b = map(int, input().split())
    c[b] +=1
    arr[a].append(b)

ans = []
for i in range(1,len(c)):
    if c[i] == 0:
        c[i] = -1
        q.appendleft(i)

while len(q) >0:
    t = q.pop()
    ans.append(t)
    for i in arr[t]:
        c[i] -=1

    for i in range(1, len(c)):
        if c[i] == 0:
            c[i] = -1
            q.appendleft(i)

print(*ans)