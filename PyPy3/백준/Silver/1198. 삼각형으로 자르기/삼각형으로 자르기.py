import heapq
import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def area(arr):
    a = 0
    for i in range(len(arr)):
        a += arr[i-1][0] * arr[i][1]
        a -= arr[i-1][1] * arr[i][0]

    a = abs(a)
    a /= 2
    return a

n = int(input())
arr = []
for i in range(n):
    a,b = map(int, input().split())
    arr.append((a,b))

maxa = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i==j or j==k or k==i:
                continue
            maxa = max(maxa, area([arr[i], arr[j], arr[k]]))

print(maxa)