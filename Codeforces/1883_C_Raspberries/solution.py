import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

INF = int(1e9)
times = int(input())
for time in range(times):
    n,k = map(int,input().split())
    dp = [INF for i in range(k)]
    arr = list(map(int,input().split()))
    for i in range(k):
        dp[i] = (i - (arr[0] % k) +k ) % k
    for i in range(1,n):
        now = arr[i]
        dp2 = [INF for i in range(k)]
        for j in range(k): #j는 나머지
            if dp[j] == INF:
                continue
            for q in range(k): #q는 now에서 나머지
                cost = (q - (now % k) + k) % k
                newr = (j * q) % k
                dp2[newr] = min(dp2[newr], dp[j] + cost)
        dp = dp2[:]
    print(dp[0])