import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def bin(p,q):
    global k
    if p>=q:
        return q
    x= (p+q)//2
    t = 1
    now = arr[0]
    for i in arr:
        if now+x<=i:
            t += 1
            now = i
    if t<k:
        return bin(p,x)
    else:
        return bin(x+1,q)


n,k = map(int, input().split())
arr= []
for i in range(n):
    arr.append(int(input()))

arr = sorted(arr)
print(bin(0, arr[-1]+1)-1)