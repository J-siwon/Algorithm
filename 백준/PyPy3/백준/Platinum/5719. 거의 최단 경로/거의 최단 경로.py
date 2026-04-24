import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n,m = map(int, input().split())
while(m !=0 or n != 0):
    s,e = map(int,input().split())
    arr =[]
    for i in range(m):
        a,b,c = map(int, input().split())
        arr.append((a,b,c))

    dist = [1e9 for i in range(n)]
    shortest = [set() for i in range(n)]
    d2 = [1e9 for i in range(n)]
    dist[s] = 0
    d2[s] = 0

    for i in range(n):
        for j in arr:
            if dist[j[1]] == dist[j[0]] + j[2]:
                shortest[j[1]].add(j[0])
            if dist[j[1]] > dist[j[0]] + j[2]:
                dist[j[1]] = dist[j[0]] + j[2]
                shortest[j[1]] = set()
                shortest[j[1]].add(j[0])

    visited = [0 for i in range(n)]
    q= deque()
    q.appendleft(e)
    while(len(q) >0):
        t = q.pop()
        if t == s:
            continue

        for i in shortest[t]:
            for j in range(len(arr)-1, -1,-1):
                if i == arr[j][0] and t == arr[j][1]:
                    arr.pop(j)
            if visited[i] == 1:
                continue
            q.appendleft(i)
            visited[i] = 1

    for i in range(n):
        for j in arr:
            if d2[j[1]] > d2[j[0]] + j[2]:
                d2[j[1]] = d2[j[0]] + j[2]

    x = d2[e]
    if x > 1e8:
        print(-1)
    else:
        print(x)
    n,m = map(int,input().split())