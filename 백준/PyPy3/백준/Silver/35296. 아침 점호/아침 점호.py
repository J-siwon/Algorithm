import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [[] for i in range(n)]
for i in range(n):
    arr[i] = list(input().strip())

todo = []
for j in range(m):
    for i in range(n):
        if arr[i][j] == "X":
            todo.append(i+n*j+1)
before = -2
ismaking = False
ans = []
for i in range(len(todo)):
    if todo[i] % n == 1 and m != 1:
        if ismaking:
            ans.append([1, before])
            before = todo[i]
        else:
            before = todo[i]
            ismaking = True
        continue

    if ismaking:
        if todo[i] == before + 1:
            ismaking = False
            ans.append([2, before, todo[i]])
        else:
            ans.append([1, before])
            before = todo[i]
    else:
        before = todo[i]
        ismaking = True

if ismaking:
    ans.append([1, before])

print(len(ans))
for i in ans:
    print(*i)