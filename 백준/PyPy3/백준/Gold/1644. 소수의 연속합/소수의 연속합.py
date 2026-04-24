import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
prime = [i for i in range(n+1)]

for i in range(2,int(n**(1/2))+1):
    if prime[i] == 0:
        continue
    for j in range(2*i, n+1, i):
        prime[j] = 0

parr = [0]
for i in range(2,len(prime)):
    if prime[i] != 0:
        parr.append(i)

dp = [0 for i in range(len(parr))]
if len(parr)>2:
    dp[1] = 2
for i in range(2,len(dp)):
    dp[i] = dp[i-1] + parr[i]


count = 0
low = len(parr) - 2
high = len(parr) - 1
while (low < high):
    if low < 0:
        break
    if dp[high] - dp[low] < n:
        low -= 1
    elif dp[high] - dp[low] > n:
        high -= 1
    else:
        low -= 1
        count += 1

if n==2:
    print(1)
else:
    print(count)