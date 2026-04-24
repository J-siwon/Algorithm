import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
isprime = False
for i in range(n):
    for j in range(i+1,n):
        maxq = 1
        a,b = arr[i], arr[j]
        for q in range(1, min(a, b) + 1):
            if a % q == 0 and b % q == 0:
                maxq = q

        t = b * (a // maxq)
        isprime = False
        for q in range(2,t):
            if t % q ==0:
                isprime = True
                break

        if isprime:
            print("YES")
            print(2)
            print(a,b)
            break
    if isprime:
        break

if not isprime:
    print("NO")