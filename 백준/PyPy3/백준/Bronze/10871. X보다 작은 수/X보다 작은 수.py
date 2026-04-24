import sys
import math
from collections import deque
input = sys.stdin.readline

x,y = map(int, input().split())
arr = list(map(int, input().split()))

for i in arr:
    if i < y:
        print(i, end= " ")