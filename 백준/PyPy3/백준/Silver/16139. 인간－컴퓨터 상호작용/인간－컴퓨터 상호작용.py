import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

alpha = "abcdefghijklmnopqrstuvwxyz"
s = input().strip()

dp = [[0 for i in range(len(alpha))] for i in range(len(s))]

n = int(input())

for i in range(len(s)):
    if i > 0:
        dp[i] = dp[i-1].copy()
    for j in range(len(alpha)):
        if alpha[j] == s[i]:
            dp[i][j] += 1

for i in range(n):
    a, x, y = input().split()
    x = int(x)
    y = int(y)
    index = 0
    for j in range(len(alpha)):
        if a == alpha[j]:
            index = j
            break
    if x == 0:
        print(dp[y][index] - 0)
    else:
        print(dp[y][index] - dp[x-1][index])