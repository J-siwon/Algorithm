import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

x = int(input())
arr = []
for i in range(9):
    arr.append(int(input()))

print(x- sum(arr))