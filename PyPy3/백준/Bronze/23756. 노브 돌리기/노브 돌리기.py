import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

a = 0
n = int(input())
a0 = int(input())
for i in range(n):
    x = int(input())
    t1 = x-a0
    t2 = a0-x
    if t1<0:
        t1 = t1+360
    if t2<0:
        t2 = t2+360

    t= min(t1,t2)
    a += t
    a0 = x

print(a)