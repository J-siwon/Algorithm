import sys
from collections import deque
input = sys.stdin.readline

x = int(input())
arr = deque()

temp = list(map(int, input().split()))
element = list(map(int, input().split()))
for i in range(x):
    if temp[i] == 0:
        arr.append(element[i])

y = int(input())
element2 = list(map(int, input().split()))
for i in range(y):
    a = element2[i]
    arr.appendleft(a)
    print(arr.pop(), end=' ')