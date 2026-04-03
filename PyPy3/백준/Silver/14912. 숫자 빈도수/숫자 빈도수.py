import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n, k = map(int,input().split())
arr = [str(i) for i in range(1, n+1)]
count = 0
for i in arr:
    for j in i:
        if j == str(k):
            count +=1

print(count)