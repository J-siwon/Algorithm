import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr.sort()
arr2.sort(reverse=True)
s = 0
for i in range(n):
    s += arr[i] * arr2[i]
print(s)