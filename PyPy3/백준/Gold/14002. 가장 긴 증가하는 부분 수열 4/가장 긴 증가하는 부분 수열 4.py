import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[] for i in range(n)]
maxlen = 0
dp[0].append(arr[0])

for i in range(1,n):
    if arr[i] < dp[0][-1]:
        dp[0].append(arr[i])
        continue
    for j in range(1,n):
        if j == n-1:
            dp[j].append(arr[i])
            maxlen = j
            break

        if len(dp[j]) ==0:
            if arr[i] > dp[j-1][-1]:
                dp[j].append(arr[i])
                maxlen = j
            break

        if dp[j-1][-1] < arr[i] < dp[j][-1]:
            dp[j].append(arr[i])
            break

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