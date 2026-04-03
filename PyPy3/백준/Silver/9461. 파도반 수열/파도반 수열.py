import sys
import math
from collections import deque
input = sys.stdin.readline

arr = [0,1,1,1,2,2,3,4,5,7,9]
for i in range(92):
    arr.append(arr[-5] + arr[-1])

x = int(input())
for i in range(x):
    t = int(input())
    print(arr[t])