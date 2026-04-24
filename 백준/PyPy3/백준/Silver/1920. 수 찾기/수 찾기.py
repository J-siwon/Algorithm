import sys
import math
from collections import deque
input = sys.stdin.readline


def Search(i,j,x):
    if i>=j :
        if arr[i] == x:
            return 1
        else:
            return 0
        
    if x < arr[(i+j)//2]:
        return Search(0,(i+j+1)//2-1,x)
    elif x > arr[(i+j)//2]:
        return Search((i+j)//2+1,j,x)
    else:
        return 1

x = int(input())
arr = list(map(int, input().split()))
y = int(input())
arr2 = list(map(int, input().split()))

arr = sorted(arr)

for i in arr2:
    print(Search(0, len(arr)-1, i))

