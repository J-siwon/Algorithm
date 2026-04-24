import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
s = 0
arr = [[] for i in range(n)]
for i in range(n):
    x, *arr[i] = map(int, input().split())

arr =sorted(arr, key = lambda x: sum(x))
for i in range(len(arr)):
    for j in range(i+1):
        s += sum(arr[j])
print(s)