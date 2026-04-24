import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def bin(i,j):
    global n, k
    if i>=j:
        return j

    x = (i+j)//2
    t1 = 0
    t2 = 0

    for p in range(1,n+1):
        t1 += bin2(p,x,0,n+1)

    for p in range(1,n+1):
        if x%p ==0 and x//p <= n:
            t2+=1

    if t1-t2 >= k:
        return bin(i,x)
    elif t1<k:
        return bin(x+1,j)
    else:
        return x

def bin2(t,k,i,j):
    global n
    if i>=j:
        if i > n:
            return n
        else:
            return j-1
    x = (i+j)//2
    if x*t<=k:
        return bin2(t,k,x+1,j)
    else:
        return bin2(t,k,i,x)

n = int(input())
k = int(input())

print(bin(0,n**2+1))