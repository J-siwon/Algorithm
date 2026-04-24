import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

times= int(input())
for time in range(times):
    n,m,k = map(int,input().split())
    arr = "L" + input().strip() + "L"
    dp = [-1 for i in range(n+2)]
    dp[0] = k
    for i in range(1,n+2):
        #log check
        isdone = False
        for j in range(max(0,i-m), i):
            if arr[j] == "L" and dp[j] >= 0:
                dp[i] = max(dp[i],dp[j])
                isdone = True
        if isdone:
            continue

        #water check
        if arr[i-1] == "W" and dp[i-1] > 0:
            dp[i] = dp[i-1]-1

    if dp[-1] >= 0:
        print("YES")
    else:
        print("NO")