import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())

arr = [[0,0,0]]
for i in range(1,x+1):
    temparr = list(map(int, input().split()))
    arr.append([min(arr[i-1][1] + temparr[0], arr[i-1][2] + temparr[0]),
                min(arr[i-1][0] + temparr[1], arr[i-1][2] + temparr[1]),
                min(arr[i-1][0] + temparr[2], arr[i-1][1] + temparr[2])])
    
print(min(arr[x]))