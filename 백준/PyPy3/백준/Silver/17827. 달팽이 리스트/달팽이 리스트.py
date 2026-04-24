import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n,m,k = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(m):
    x = int(input())
    if x >= n:
        t = (x-k+1) % (n-k+1)
        x = t+k-1
    print(arr[x])
