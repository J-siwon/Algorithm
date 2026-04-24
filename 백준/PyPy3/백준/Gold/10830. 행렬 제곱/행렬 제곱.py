import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def nPow(arr1, b):
    if b==1:
        return arr1
    else:
        if b% 2 ==0:
            return Pow(nPow(arr1,b//2))
        else:
            return Mul(Pow(nPow(arr1,(b-1)//2)), arr1)

def Mul(arr1, arr2):
    global n
    arr3 = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for q in range(n):
                arr3[i][j] += arr1[i][q] * arr2[q][j]
            arr3[i][j] = arr3[i][j] % 1000

    return arr3

def Pow(arr1):
    global n
    #결과 arr2
    arr2 = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for q in range(n):
                arr2[i][j] += arr1[i][q] * arr1[q][j]
            arr2[i][j] = arr2[i][j] % 1000

    return arr2


n,b = map(int, input().split())
arr1 = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    arr1[i] = list(map(int,input().split()))

arr = nPow(arr1, b)
for i in range(n):
    for j in range(n):
        arr[i][j] %= 1000
        
for i in range(n):
    print(*arr[i])
