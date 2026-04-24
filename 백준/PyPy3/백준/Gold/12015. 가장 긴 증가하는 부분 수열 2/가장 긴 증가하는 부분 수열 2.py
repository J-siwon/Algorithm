import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def bin(arr,q,i,j):
    if i>=j:
        return j
    x = (i+j)//2
    if arr[x] >=q:
        return bin(arr,q,i,x)
    else:
        return bin(arr,q,x+1,j)

n = int(input())
k = list(map(int, input().split()))

arr = [k[0]]
for q in range(len(k)):
    p = bin(arr,k[q],0,len(arr))
    if p == len(arr):
        arr.append(k[q])
    else:
        arr[p] = k[q]

print(len(arr))