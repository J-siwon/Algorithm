import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[1e9] for i in range(n)]
maxlen = 0
dp[0].append(arr[0])

for i in range(1,n):
    if arr[i] < dp[0][-1]:
        dp[0].append(arr[i])
        continue

    low = 0
    high = n-1
    while(low < high):
        mid = (low + high) //2
        if arr[i] <= dp[mid][-1]:
            high = mid
        else:
            low = mid + 1

    if low == n-1:
        dp[low].append(arr[i])
        maxlen = low
    elif len(dp[low]) ==1:
        dp[low].append(arr[i])
        maxlen = low
    else:
        dp[low].append(arr[i])


print(maxlen+1)
minnum = dp[maxlen][-1]
ans = []
ans.append(minnum)
for i in range(maxlen-1, -1, -1):
    while len(dp[i]) > 0 and minnum > dp[i][-1]:
        t = dp[i].pop()
    minnum = t
    ans.append(minnum)
ans.reverse()
print(*ans)