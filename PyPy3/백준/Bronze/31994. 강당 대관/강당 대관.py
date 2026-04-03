import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

arr = []
for i in range(7):
    a,b = input().split()
    arr.append([a,b])

arr = sorted(arr, key= lambda x:int(x[1]))
print(arr[-1][0])