import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

def go(a,b):
    return dist(arr[a], arr[b])

def dist(x,a):
    return ((x[0]-a[0])**2 + (x[1]-a[1])**2)**(1/2)

arr = []
for i in range(4):
    arr.append(list(map(int,input().split())))
case = []
case.append(go(0,1) + go(1,2) + go(2,3))
case.append(go(0,1) + go(1,3) + go(3,2))
case.append(go(0,2) + go(2,1) + go(1,3))
case.append(go(0,2) + go(2,3) + go(3,1))
case.append(go(0,3) + go(3,1) + go(1,2))
case.append(go(0,3) + go(3,2) + go(2,1))

print(math.floor(min(case)))