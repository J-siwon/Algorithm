import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
maxn = 0
count = 0
while len(arr) > 0:
    t = arr.pop()
    count +=1
    maxn = max(maxn, t*count)
print(maxn)
