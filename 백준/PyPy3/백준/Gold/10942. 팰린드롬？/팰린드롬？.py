import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[0 for i in range(n)] for i in range(n)]


for i in range(n):
    dp[i][i] = 1

for i in range(1,n):
    if arr[i-1] == arr[i]:
        dp[i-1][i] = 1

for k in range(2,n):
    for i in range(n-k):
        if arr[i] == arr[i+k]:
            dp[i][i+k] = 1
        else:
            dp[i][i + k] = 0
            continue

        if dp[i+1][i+k-1] == 0:
            dp[i][i+k] = 0

for i in range(int(input())):
    a,b = map(int, input().split())
    print(dp[a-1][b-1])