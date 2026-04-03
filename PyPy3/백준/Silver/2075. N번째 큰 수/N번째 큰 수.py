import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
h = list(map(int,input().split()))
heapq.heapify(h)
for i in range(1,n):
    for j in map(int, input().split()):
        x = heapq.heappop(h)
        heapq.heappush(h,max(x,j))

print(heapq.heappop(h))
