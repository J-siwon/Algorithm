import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())

r = list(map(int, input().split()))
v = list(map(int, input().split()))
arr = v[0]
val = v[0] * r[0]
for i in range(1,len(r)):
    arr = min(arr, v[i])
    val += arr * r[i]

print(val)