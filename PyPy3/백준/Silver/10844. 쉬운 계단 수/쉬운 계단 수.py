import sys
import math
from collections import deque
input = sys.stdin.readline

arr = [0,1,1,1,1,1,1,1,1,1]
x = int(input())
for i in range(1,x):
    temparr = [0,0,0,0,0,0,0,0,0,0]
    temparr[0] = arr[1]
    temparr[-1] = arr[-2]
    for j in range(1,len(arr)-1):
        temparr[j] = arr[j-1] + arr[j+1]
    arr = temparr.copy()
print(sum(arr)%1000000000)