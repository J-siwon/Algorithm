import sys
input = sys.stdin.readline

n = int(input())
dp = [(0,1) for i in range(n)]

for i in range(1,n):
    dp[i] = (dp[i-1][1], dp[i-1][0]+dp[i-1][1])

print(*dp[-1])