import sys
import math
from collections import deque
input = sys.stdin.readline

x,y = map(int, input().split())
arr = list(map(int, input().split()))

temparr = [0]
sum = 0
for i in arr:
    sum+=i
    temparr.append(sum)
for i in range(y):
    a,b = map(int, input().split())
    print(temparr[b] - temparr[a-1])