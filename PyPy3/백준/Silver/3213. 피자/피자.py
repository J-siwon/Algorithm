import sys
import math
from collections import deque, Counter

n = int(input())
isleft = [False,0,0]
count = 0
arr = []
for i in range(n):
    a,b = map(int,input().split('/'))
    arr.append([a,b])
arr = sorted(arr, key = lambda x: (-x[0], x[1]))

for i in arr:
    a = i[0]
    b = i[1]
    if b ==2:
        if isleft[0]:
            isleft[0] = False
        else:
            count+= 1
            isleft[0] = True
    else:
        if a==1:
            if isleft[1]>0:
                isleft[1] -=1
            else:
                if isleft[0]:
                    isleft[0] = False
                    isleft[1] +=1
                elif isleft[2] >0:
                    isleft[2]-=1
                    isleft[0] = True
                else:
                    count +=1
                    isleft[2] +=1
        else:
            if isleft[2] >0:
                isleft[2]-=1
            else:
                isleft[1] +=1
                count +=1
print(count)