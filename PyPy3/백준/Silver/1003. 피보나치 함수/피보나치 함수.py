import sys
import math
from collections import deque
input = sys.stdin.readline

t = int(input())
arr = [1,0,1,1,2]
def fibo(n):
    if len(arr) > n+1:
        return [arr[n], arr[n+1]]
    else:
        for i in range(len(arr), n+2):
            arr.append(arr[i-1]+arr[i-2])
        return [arr[n], arr[n+1]]


for i in range(t):
    x = int(input())
    print(*fibo(x))