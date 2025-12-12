import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

def Swap(arr,i,j):
    tmp = arr[j]
    arr[j] = arr[i]
    arr[i] = tmp

def Push(arr,x):
    arr.append(x)
    index = len(arr)
    while(index//2>0):
        if arr[index-1][0] < arr[index//2-1][0]:
            Swap(arr,index-1, index//2-1)
            index = index//2
        else:
            if arr[index-1][0] == arr[index//2-1][0] and arr[index-1][1] < arr[index//2-1][1]:
                Swap(arr,index-1, index//2-1)
                index = index//2
            else:
                break

def Pop(arr):
    if len(arr) >0:
        Swap(arr,0,-1)
        x = arr.pop()
        index = 1
        newindex = Find(arr,index)
        while(newindex != index):
            Swap(arr, newindex-1, index-1)
            index = newindex
            newindex = Find(arr,index)
    else:
        x = arr.pop()
    return x

def Find(arr,index):
    left = index*2
    right = index*2+1
    if left <= len(arr) and arr[left-1][0] < arr[index-1][0]:
        index = left
    else:
        if left <= len(arr) and arr[left - 1][0] == arr[index-1][0] and arr[left - 1][1] < arr[index- 1][1]:
            index = left

    if right <= len(arr) and arr[right-1][0] < arr[index-1][0]:
        index = right
    else:
        if right <= len(arr) and arr[right - 1][0] == arr[index - 1][0] and arr[right - 1][1] < arr[index - 1][1]:
            index = right
    return index

arr= []
for i in range(int(input())):
    x = int(input())
    if x == 0:
        if len(arr)>0:
            print(Pop(arr)[1])
        else:
            print(0)
    else:
        Push(arr,[abs(x),x])
