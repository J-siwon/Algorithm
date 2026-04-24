import sys
import math
from collections import deque
input = sys.stdin.readline

n,k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

count = 0
for i in range(len(coins)-1, -1, -1):
    count += k // coins[i] 
    k = k % coins[i]

print(count)