import sys
import math
from collections import deque
input = sys.stdin.readline

def BackTracking(arr):
    if len(arr) == y:
        print(*arr)
        return
    
    for i in range(1,x+1):
        arr.append(i)
        BackTracking(arr)
        arr.pop()

x, y = map(int, input().split())
arr = []
BackTracking(arr)