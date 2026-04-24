import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

t = -1e9
if a%c==0:
    t = a//c
else:
    t = a//c +1

if b%d==0:
    t = max(t, b//d)
else:
    t = max(t, b//d+1)
print(l-t)
