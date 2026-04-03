import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [int(1e9) for i in range(n)]
dp[0] = arr[0]
ans = [1e9 for i in range(n)]
ans[0] = arr[0]
maxlen = 1
for i in range(1,len(arr)):
    low = 0
    high = n-1
    while(low < high):
        mid = (low+high) // 2
        if dp[mid] >= arr[i]:
            high = mid
        else:
            low = mid + 1

    if low > 0 and low < n-1 and dp[low-1] < arr[i] < dp[low+1] and arr[i] < dp[low]:
        dp[low] = arr[i]
        if maxlen <= low+1:
            maxlen = low+1
            ans[low] = arr[i]
            while(low > 0 and ans[low-1] >= ans[low]):
                ans[low-1] = dp[low-1]
                low -=1

    if low == 0:
        if dp[low] > arr[i]:
            dp[low] = arr[i]

    if low == n-1:
        if dp[low] == int(1e9):
            dp[low] = arr[i]
            maxlen = n
            ans[low] = arr[i]
            while (low > 0 and ans[low - 1] >= arr[i]):
                ans[low - 1] = dp[low - 1]
                low -= 1


print(maxlen)