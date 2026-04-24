import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

for i in range(int(input())):
    a,b = map(int,input().split())
    t = a%10
    for j in range(b-1):
        t = (t*a)%10
    if t ==0:
        print(10)
    else:
        print(t)