import sys
import math
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
arr = dict()
for i in range(n):
    x, y = input().strip().split()
    arr[x] = y

for k in range(k):
    print(arr[input().strip()])