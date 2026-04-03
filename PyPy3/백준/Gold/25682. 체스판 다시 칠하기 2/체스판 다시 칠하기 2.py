import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

r,c,n= map(int,input().split())

arr = ["B"*c for i in range(r)]
for i in range(r):
    arr[i] = input().strip()

dp = [[0 for i in range(c)] for i in range(r)]
#case 1 왼쪽 위가 W 시작
for i in range(r):
    for j in range(c):
        if i%2==0:
            if j%2==0:
                #W
                if arr[i][j] == "W":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
            else:
                #B
                if arr[i][j] == "B":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1

        else:
            if j%2 ==0:
                #B
                if arr[i][j] == "B":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
            else:
                #W
                if arr[i][j] == "W":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1

for i in range(len(dp)):
    for j in range(1,len(dp[0])):
        dp[i][j] = dp[i][j-1] + dp[i][j]

for i in range(1,len(dp)):
    for j in range(len(dp[0])):
        dp[i][j] = dp[i-1][j] + dp[i][j]
x1 = []
for i in range(r-n+1):
    for j in range(c-n+1):
        if i==0:
            if j==0:
                x1.append(dp[n - 1][n - 1])
            else:
                x1.append(dp[n-1][n-1+j] - dp[n-1][j-1])
        else:
            if j==0:
                x1.append(dp[n-1+i][n-1] - dp[i-1][n-1])
            else:
                x1.append(dp[n-1+i][n-1+j] - dp[i-1][n-1+j] - dp[n-1+i][j-1] + dp[i-1][j-1])


# case 2 왼쪽 위가 B 시작
dp = [[0 for i in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        if i % 2 == 0:
            if j % 2 == 0:
                # B
                if arr[i][j] == "B":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
            else:
                # W
                if arr[i][j] == "W":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
        else:
            if j % 2 == 0:
                # W
                if arr[i][j] == "W":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
            else:
                # B
                if arr[i][j] == "B":
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1

for i in range(len(dp)):
    for j in range(1,len(dp[0])):
        dp[i][j] = dp[i][j-1] + dp[i][j]

for i in range(1,len(dp)):
    for j in range(len(dp[0])):
        dp[i][j] = dp[i-1][j] + dp[i][j]
x2 = []

for i in range(r-n+1):
    for j in range(c-n+1):
        if i==0:
            if j==0:
                x2.append(dp[n - 1][n - 1])
            else:
                x2.append(dp[n-1][n-1+j] - dp[n-1][j-1])
        else:
            if j==0:
                x2.append(dp[n-1+i][n-1] - dp[i-1][n-1])
            else:
                x2.append(dp[n-1+i][n-1+j] - dp[i-1][n-1+j] - dp[n-1+i][j-1] + dp[i-1][j-1])

print(min(min(x1), min(x2)))