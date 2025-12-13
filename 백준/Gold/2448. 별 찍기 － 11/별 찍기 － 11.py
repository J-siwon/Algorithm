import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

def Tri(n, level):
    if n==3:
        arr[level-3] += "*"
        arr[level-2] += "* *"
        arr[level-1] += "*****"
        return

    if n %2 == 0:
        Tri(n//2, level - n//2)
        Tri(n//2, level)
        Blank(n//2, level)
        Tri(n//2, level)
        return

def Blank(n, level):
    for i in range(level-n, level):
        arr[i] += " " * ((level-i-1)*2 +1)

n = int(input())
arr = [""]*n
for i in range(len(arr)):
    arr[n-i-1] += "   " * (i//3)
    if (n-i-1) % 3 == 2:
        arr[i] += "  "
    elif (n-i-1) % 3 == 1:
        arr[i] += " "
Tri(n, n)
for i in range(len(arr)):
    arr[n-i-1] += "   " * (i//3)
    if (n-i-1) % 3 == 2:
        arr[i] += "  "
    elif (n-i-1) % 3 == 1:
        arr[i] += " "
for i in range(len(arr)):
    print(arr[i])