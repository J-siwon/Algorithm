import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
for i in range(n):
    x = int(input())
    arr = list(map(int, input().split()))
    arr2= [0] *len(arr)
    last = 0
    for i in range(x):
        for j in range(last+1,201):
            if arr[i] !=j:
                arr2[i] =j
                last = j
                break
    print(arr2[-1])