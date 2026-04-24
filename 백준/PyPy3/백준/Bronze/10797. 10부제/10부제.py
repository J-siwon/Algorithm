import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

a = int(input())
arr = list(map(int, input().split()))
count = 0
for i in arr:
    if a == i:
        count +=1
print(count)