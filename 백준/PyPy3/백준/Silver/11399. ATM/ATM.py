import sys
import math
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

count = 0
for i in range(len(arr)):
    for j in range(0,i+1):
        count += arr[j]

print(count)