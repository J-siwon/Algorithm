import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

v = int(input())
n = int(input())
t = 210

for i in range(n):
    a,b = input().split()
    a = int(a)
    t -= a
    if t <= 0:
        print(v)
        break

    if b == "T":
        v +=1
        if v > 8:
            v = 1

