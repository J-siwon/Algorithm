import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
arr = deque()

for i in range(x):
    a = list(input().split())

    if a[0] == "push":
        arr.append(int(a[1]))
    elif a[0] == "pop":
        if len(arr) > 0:
            print(arr.pop())
        else:
            print(-1)
    elif a[0]== "size":
        print(len(arr))
    elif a[0] == "empty":
        if len(arr) > 0:
            print(0)
        else:
            print(1)
    elif a[0]== "top":
        if len(arr) > 0:
            print(arr[-1])
        else:
            print(-1)