import sys
import math
input = sys.stdin.readline

x, y = map(int, input().split())
arr = []
arr2 = []
for i in range(x):
    arr.append(input().strip())

for i in range(len(arr)):
    if len(arr[i]) >= y:
        arr2.append(arr[i])

arr2 = sorted(arr2)
arr3 = dict()
for i in arr2 :
    arr3[i] = 0 
for i in range(len(arr2)-1):
    if arr2[i] == arr2[i+1]:
        arr3[arr2[i]]+=1

arr3 = sorted(arr3.items(), key = lambda a: a[1], reverse= True)
arr3 = sorted(arr3, key= lambda a: (a[1], len(a[0])), reverse= True)

for i in arr3:
    print(i[0])