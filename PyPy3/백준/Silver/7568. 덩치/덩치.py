import sys
from collections import deque
input = sys.stdin.readline

x = int(input())
arr =[]
for i in range(x):
    arr.append(list(map(int, input().split())))

score = [1] * x
for i in range(len(arr)):
    for j in arr:
        if arr[i][0] < j[0] and arr[i][1] < j[1]:
            score[i] += 1

print(*score)
