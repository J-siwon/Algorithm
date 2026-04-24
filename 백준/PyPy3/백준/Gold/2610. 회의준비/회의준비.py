import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

def dijk(startv):
    d = [1e9 for i in range(n)]
    q = [(0,startv)]
    d[startv-1] = 0

    while(len(q)>0):
        t = heapq.heappop(q)
        cost = t[0]
        now = t[1]

        if cost > d[now-1]:
            continue

        for i in arr[now-1]:
            if d[i-1] > cost + 1:
                d[i-1] = cost + 1
                heapq.heappush(q, (cost+1,i))

    return d


n = int(input())
arr = [[]for i in range(n)]

m = int(input())
for i in range(m):
    a,b = map(int, input().split())
    arr[b-1].append(a)
    arr[a-1].append(b)

visited = [0 for i in range(n)]
groups = []
for i in range(n):
    tempd = dijk(i+1)
    tempgroup = []
    for j in range(len(tempd)):
        if tempd[j] < 1e8:
            tempgroup.append(j)

    if tempgroup not in groups:
        groups.append(tempgroup)

totalsum = 0
boss = []
for i in groups:
    groupmax = 1e9
    groupboss = i[0]
    for j in i:
        tempd = dijk(j+1)
        tempmax = 0

        for k in i:
            tempmax = max(tempmax, tempd[k])

        if groupmax > tempmax:
            groupboss = j
            groupmax = tempmax

    boss.append(groupboss+1)

boss.sort()
print(len(boss))
for i in range(len(boss)):
    print(boss[i])
