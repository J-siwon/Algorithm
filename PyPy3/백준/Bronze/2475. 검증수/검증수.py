import sys
import math
from collections import deque
input = sys.stdin.readline

arr = list(map(int, input().split()))
add = 0
for i in arr:
    add += i**2

print(add%10)