import sys
import math
from collections import deque
input = sys.stdin.readline

def BackTrack(arr):
    if(len(arr) == y):
        print(*arr)
        return
    for i in range(1,x+1):
        if len(arr) > 0:
            if i <= arr[-1]:
                continue
        arr.append(i)
        BackTrack(arr)
        arr.pop()
    
    
x, y = map(int, input().split())
arr = []
BackTrack(arr)