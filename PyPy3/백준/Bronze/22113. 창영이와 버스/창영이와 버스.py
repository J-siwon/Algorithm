import sys
import math
from collections import deque, Counter

n,m = map(int, input().split())
num = list(map(int, input().split()))
arr = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int, input().split()))

count = 0
for i in range(1, len(num)):
    count += arr[num[i-1]-1][num[i]-1]
print(count)