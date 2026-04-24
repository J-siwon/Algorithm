import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def bin(i,j):
    global k
    if i>=j:
        return j
    x = (i+j)/2
    t = 0
    for q in arr:
        t += q//x
    if t>=k:
        return bin((i+j)//2+1,j)
    else:
        return bin(i,(i+j)//2)


n, k = map(int,input().split())
t = 0
arr = []
for i in range(n):
    x = int(input())
    t+=x
    arr.append(x)

t = t//k
ans = bin(1,t)
r = 0
for i in arr:
    r += i//ans
if r < k:
    ans -=1
print(ans)
# 이분 탐색으로 1~t 범위 내에서
