import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

s = input().strip()
arr = list(s.split("-"))

for i in range(len(arr)):
    arr[i] = sum(map(int, arr[i].split("+")))

x = arr[0]

for i in range(1, len(arr)):
    x -= arr[i]
print(x)