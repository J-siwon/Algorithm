import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())


for j in range(x):
    isdone = False
    count = 0
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = deque()

    for i in range(len(arr)):
        arr2.append((i, arr[i]))

    while not isdone :
        jump = False
        t = arr2.popleft()
        for i in range(10,t[1],-1):
            for j in range(len(arr2)):
                if arr2[j][1] == i:
                    arr2.append(t)
                    jump = True
                    break
            
            if jump:
                break
        
        if jump:
            continue

        if t[0] == b:
            print(count+1)
            isdone = True
        else:
            count+=1
