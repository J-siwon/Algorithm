import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

arr = [i for i in range(1,21)]
for i in range(10):
    a, b = map(int, input().split())
    t = (a+b)//2 
    for j in range(a-1,t):
        (arr[j], arr[b-(j-a+1)-1]) = (arr[b-(j-a+1)-1], arr[j])
print(*arr)