import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())

length = [1e9 for i in range(n+1)]
maxlen = 1
arr = list(map(int,input().split()))
length[0] = 0
for i in arr:
    for j in range(1,len(length)):
        if length[j-1] < i <length[j]:
            length[j] = i
            maxlen = max(maxlen,j)

print(maxlen)