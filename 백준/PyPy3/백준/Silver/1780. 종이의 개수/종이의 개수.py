import sys
import math
from collections import deque, Counter
input = sys.stdin.readline


def Devide(arr):
    global t1
    global t2
    global t3

    n = len(arr)
    if n==1:
        if arr[0][0] == -1:
            t1+=1
        elif arr[0][0] == 0:
            t2 +=1
        elif arr[0][0] == 1:
            t3 +=1
        return

    if arr[0][0] == -1:
        s = 0
        id = True
        for i in range(n):
            for j in range(n):
                if arr[i][j] != -1:
                    id =False
                    break
            if not id:
                break
        if id:
            t1 +=1
            return
    elif arr[0][0] == 0:
        s = 0
        id = True
        for i in range(n):
            for j in range(n):
                if arr[i][j] != 0:
                    id = False
                    break
            if not id:
                break
        if id:
            t2 += 1
            return
    elif arr[0][0] == 1:
        s = 0
        id = True
        for i in range(n):
            for j in range(n):
                if arr[i][j] != 1:
                    id = False
                    break
            if not id:
                break
        if id:
            t3 += 1
            return

    if len(arr)==3:
        for i in range(3):
            for j in range(3):
                Devide([[arr[i][j]]])
        return

    for i in range(0, 3):
        for j in range(0, 3):
            t = [[0 for k in range(len(arr)//3)] for k in range(len(arr)//3)]
            for p in range(0, len(arr)//3):
                for q in range(0, len(arr)//3):
                    t[p][q] = arr[len(arr)//3 * i + p][len(arr)//3 * j + q]
            Devide(t)

n = int(input())
arr = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    arr[i] = list(map(int, input().split()))

t1 = 0
t2 = 0
t3 = 0
Devide(arr)
print(t1)
print(t2)
print(t3)