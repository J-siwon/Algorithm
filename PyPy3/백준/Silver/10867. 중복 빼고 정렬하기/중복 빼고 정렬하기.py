import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = set()
for i in range(n):
    ans.add(arr[i])

print(*ans)