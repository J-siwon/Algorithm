import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs (graph, e, visittime):
    global times
    visittime[e-1] = times
    for i in graph[e]:
        if visittime[i-1] == 0:
            times +=1
            dfs(graph, i, visittime)

n,m,r = map(int,input().split())
graph = [[] for i in range(n+1)]
times = 1
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

visittime = [0 for i in range(n)]

dfs (graph, r, visittime)

for i in range(n):
    print(visittime[i])