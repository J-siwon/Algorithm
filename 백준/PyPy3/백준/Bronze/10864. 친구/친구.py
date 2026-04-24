import sys
import math
from collections import deque
input = sys.stdin.readline

a,b = map(int, input().split())
arr = [0 for i in range(a+1)]
for i in range(b):
    x,y = map(int, input().split())
    arr[x] += 1
    arr[y] += 1

for i in range(1,a+1):
    print(arr[i])