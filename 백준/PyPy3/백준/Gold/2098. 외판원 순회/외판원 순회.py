import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline


def dfs(now, visited):
    if visited == (1<<n)-1:
        if arr[now][0] == 0:
            return 1e9
        return arr[now][0]

    if dp[now][visited] != -1:
        return dp[now][visited]

    tmcost = 1e9
    for i in range(n):
        if arr[now][i] == 0:
            continue
        t = 1<<i
        if visited & t != 0:
            continue

        cost = dfs(i,visited | t) + arr[now][i]
        tmcost = min(tmcost, cost)
    dp[now][visited] = tmcost
    return dp[now][visited]

n = int(input())
dp = [[-1 for i in range(1 << n+1 -1)] for i in range(n)]
mincost = 1e9

arr = [[] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))


mincost = dfs(0,1)

print(mincost)