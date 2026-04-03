import sys
import math
import heapq
from collections import deque, Counter

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
left = 0
right = n-1
arr.sort()
c = 0
while left != right:
    if arr[left] + arr[right] > x:
        right -=1
    elif arr[left] + arr[right] < x:
        left += 1
    else:
        c +=1
        left +=1

print(c)