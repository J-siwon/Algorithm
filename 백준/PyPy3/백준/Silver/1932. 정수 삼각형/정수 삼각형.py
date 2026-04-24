import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
arr = [int(input())]

for i in range(1,x):
    temparr = list(map(int, input().split()))
    arr.append(temparr[-1] + arr[-1])

    for j in range(i-1,0,-1):
        arr[j] = max(arr[j-1], arr[j]) + temparr[j]
    arr[0] = temparr[0] + arr[0]
    

print(max(arr))