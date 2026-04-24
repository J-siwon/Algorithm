import sys
import math
from collections import deque, Counter

n,m = map(int, input().split())
c = [0 for i in range(n)]
g = [[] for i in range(n)]
q = []
for i in range(m):
    a,b = map(int, input().split())
    g[a-1].append(b)
    c[b-1] +=1

for i in range(len(c)):
    if c[i] == 0:
        q.append(i)

q = sorted(q, reverse= True)

while(len(q)):
    t= q.pop()
    print(t+1, end = " ")
    for i in g[t]:
        c[i-1] -= 1
        if c[i-1] == 0:
            q.append(i-1)

    q = sorted(q, reverse = True)