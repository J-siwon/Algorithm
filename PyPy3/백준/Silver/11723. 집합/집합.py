import sys
import math
from collections import deque
input = sys.stdin.readline

x= int(input())

arr = set()

for i in range(x):
    lst = list(input().split())
    if len(lst) > 1:
        lst[1] = int(lst[1])

    if lst[0] == "add":
        arr.add(lst[1])
    elif lst[0] == "remove":
        if lst[1] in arr:
            arr.remove(lst[1])
    elif lst[0] == "check":
        if lst[1] in arr:
            print(1)
        else:
            print(0)
    elif lst[0] == "toggle":
        if lst[1] in arr:
            arr.remove(lst[1])
        else:
            arr.add(lst[1])
    elif lst[0] == "all":
        arr = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif lst[0] == "empty":
        arr.clear()