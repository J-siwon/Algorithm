import sys
import math
from collections import deque
input = sys.stdin.readline

def backtracking(arr):
    if len(ans) == b:
        print(*ans)
        return
    for i in range(len(arr)):
        t = arr[i]
        if t in ans:
            continue
        ans.append(t)
        backtracking(arr)
        ans.pop()

a,b = map(int, input().split())
arr= list(map(int, input().split()))

arr = sorted(arr)
ans = []
backtracking(arr)
