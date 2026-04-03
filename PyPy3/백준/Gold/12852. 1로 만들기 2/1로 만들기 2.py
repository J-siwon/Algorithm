import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
dp = [1e9 for i in range(n+1)]
dp[1] = 0
arr = [[1] for i in range(n+1)]
if n>1:
    dp[2] = 1
    arr[2] = [1,2]
if n>2:
    dp[3] = 1
    arr[3] = [1,3]
for i in range(4,n+1):
    if i%3 == 0:
        if dp[i] > dp[i//3]+1:
            dp[i] = dp[i//3]+1
            arr[i] = arr[i//3].copy()
            arr[i].append(i)
    if i%2 == 0:
        if dp[i] > dp[i//2]+1:
            dp[i] = dp[i//2]+1
            arr[i] = arr[i // 2].copy()
            arr[i].append(i)
    if dp[i] > dp[i-1]+1:
        dp[i] = dp[i-1]+1
        arr[i] = arr[i - 1].copy()
        arr[i].append(i)


print(dp[n])
print(*list(reversed(arr[n])))
