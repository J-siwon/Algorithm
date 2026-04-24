import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def Divide(arr):
    global white
    global black
    # check all 1 or all 0
    check = 0
    for i in range(len(arr)):
        check +=sum(arr[i])

    if check == 0:
        white +=1
        return
    elif check == len(arr)**2:
        black +=1
        return
    else:
        x = len(arr)//2
        arr1 = [[] for i in range(x)]
        for i in range(x):
            arr1[i] = arr[i][:x]

        arr2 = [[] for i in range(x)]
        for i in range(x):
            arr2[i] = arr[i][x:]

        arr3 = [[] for i in range(x)]
        for i in range(x,len(arr)):
            arr3[i-x] = arr[i][:x]

        arr4 = [[] for i in range(x)]
        for i in range(x, len(arr)):
            arr4[i-x] = arr[i][x:]

        Divide(arr1)
        Divide(arr2)
        Divide(arr3)
        Divide(arr4)

n = int(input())
arr = [[] for i in range(n)]
for i in range(n):
    arr[i] = list(map(int,input().split()))
white = 0
black =0
Divide(arr)
print(white)
print(black)