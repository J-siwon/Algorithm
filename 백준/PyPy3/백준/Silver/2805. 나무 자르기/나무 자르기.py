import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def bin(i,j):
    global k
    if i>=j:
        return j
    x = (i+j)//2
    t = 0
    for q in arr:
        if q-x > 0:
            t += q-x
    if t>=k:
        return bin((i+j)//2+1,j)
    else:
        return bin(i,(i+j)//2)


n, k = map(int,input().split())
arr = list(map(int, input().split()))
t = max(arr)+ k

ans = bin(1,t)

print(ans-1)