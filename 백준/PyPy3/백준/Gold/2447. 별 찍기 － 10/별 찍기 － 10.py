import sys
import math
input = sys.stdin.readline

def MakeBlank(arr, x, y, dif):
    if dif == 1:
        return arr
    
    t = dif//3
    for i in range(3):
        for j in range(3):
            if i==1 and j ==1:
                arr = Blank(arr,x+t,y+t,t)
            arr = MakeBlank(arr, x + t * i, y+ t *j, t)
    
    return arr

def Blank(arr,a,b, dif):
    for i in range(a, a+dif):
        for j in range(b,b+dif):
            arr[i][j] = " "
    return arr

x = int(input())
arr = []
for i in range(x):
    arr.append([])
    for j in range(x):
        arr[i].append("*")

arr2 = MakeBlank(arr,0,0,x)
for i in range(x):
    for j in range(x):

        print(arr2[i][j], end="")
    print()

