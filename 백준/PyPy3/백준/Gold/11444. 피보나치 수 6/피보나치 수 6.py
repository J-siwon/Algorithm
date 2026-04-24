import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def nPow(arr, n):
    if n ==1:
        return arr
    else:
        if n % 2==0:
            return nPow(Pow(arr), n//2)
        else:
            return Mul(nPow(Pow(arr),n//2), arr)

def Pow(arr):
    return Mul(arr, arr)

def Mul(arr1, arr2):
    arr3 = [[0 for i in range(2)] for i in range(2)]
    for i in range(2):
        for j in range(2):
            for q in range(2):
                arr3[i][j] += arr1[i][q] * arr2[q][j]
            arr3[i][j] %= 1000000007
    return arr3

arr = [[1,1], [2,3]]
x = int(input())
if x==1:
    print(arr[0][0])
elif x==2:
    print(arr[0][1])
elif x==3:
    print(arr[1][0])
elif x==4:
    print(arr[1][1])
else:
    t = nPow([[0, 1], [1, 1]], x - 1)
    print(Mul(arr,t)[0][0])