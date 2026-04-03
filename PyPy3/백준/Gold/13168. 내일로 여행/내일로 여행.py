import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n,r = map(int, input().split())

arr = list(input().split())

dic = dict()
x = 0
for i in range(n):
    if arr[i] not in dic:
        dic[arr[i]] = x
        x += 1

arr = [[1e9 for i in range(len(dic))] for i in range(len(dic))]
arr2 = [[1e9 for i in range(len(dic))] for i in range(len(dic))]

tovisit = []
_ = int(input())
for j in input().split():
    tovisit.append(dic[j])

for i in range(int(input())):
    type,start,end,w = input().split()

    a = dic[start]
    b = dic[end]
    w = int(w)

    arr[a][b] = min(arr[a][b], w)
    arr[b][a] = min(arr[b][a], w)

    if type == "S-Train" or type == "V-Train":
        arr2[a][b] = min(arr2[a][b], (w+1) // 2)
        arr2[b][a] = min(arr2[b][a], (w+1) // 2)
    elif type == "Mugunghwa" or type == "ITX-Saemaeul" or type == "ITX-Cheongchun":
        arr2[a][b] = 0
        arr2[b][a] = 0
    else:
        arr2[a][b] = min(arr2[a][b], w)
        arr2[b][a] = min(arr2[b][a], w)

for i in range(len(dic)):
    arr[i][i] = 0
    arr2[i][i] = 0

for k in range(len(dic)):
    for i in range(len(dic)):
        for j in range(len(dic)):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

            if arr2[i][j] > arr2[i][k] + arr2[k][j]:
                arr2[i][j] = arr2[i][k] + arr2[k][j]

cost1 = 0
cost2 = 0
for i in range(1,len(tovisit)):
    a = tovisit[i-1]
    b= tovisit[i]
    cost1 += arr[a][b]
    cost2 += arr2[a][b]

if cost1 <= cost2 + r:
    print("No")
else:
    print("Yes")