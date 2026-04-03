import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

count1 = 0
for i in arr:
    if i %a == 0:
        count1 += i // a
    else:
        count1 += i // a + 1

print(count1)
print(x // b, end = " ")
print(x % b)