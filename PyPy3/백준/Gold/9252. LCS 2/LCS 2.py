import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

if len(s2) > len(s1):
    t = s1
    s1 = s2
    s2 = t

arr1 = [0 for i in range(len(s1))]
a1 = [("",1) for i in range(len(s1))]
arr2 = [0 for i in range(len(s2))]
a2 = [("",-1) for i in range(len(s2))]

for i in range(len(s1)):
    used = 1
    arr2 = [0 for i in range(len(s2))]
    a2 = [("",-1) for i in range(len(s2))]
    if s1[i] == s2[0]:
        arr2[0] = 1
        used = 0
        a2[0] = (s2[0],0)
    else:
        a2[0] = a1[0]
    for j in range(1,len(s2)):
        if s1[i] == s2[j]:
            if a1[j][1] >= j: #위에서 사용
                if arr1[j] > arr2[j-1] + used:
                    arr2[j] = arr1[j]
                    a2[j] = a1[j]
                else:
                    if used == 1:
                        arr2[j] = arr2[j-1] + 1
                        a2[j] = (a2[j-1][0] + s2[j], j)
                        used = 0
                    else:
                        arr2[j] = arr2[j-1]
                        a2[j] = a2[j-1]
            else:
                if arr1[j] +1 > arr2[j-1] + used:
                    arr2[j] = arr1[j] + 1
                    a2[j] = (a1[j][0] + s2[j], j)
                    used = 0
                else:
                    if used == 1:
                        arr2[j] = arr2[j - 1] + 1
                        a2[j] = (a2[j - 1][0] + s2[j], j)
                        used = 0
                    else:
                        arr2[j] = arr2[j - 1]
                        a2[j] = a2[j - 1]

        else:
            if arr2[j-1] >= arr1[j]:
                arr2[j] = arr2[j-1]
                a2[j] = a2[j-1]
            else:
                arr2[j] = arr1[j]
                a2[j] = a1[j]

    for j in range(len(arr2)):
        arr1[j] = arr2[j]
        a1[j] = a2[j]



print(len(a2[-1][0]))
if len(a2[-1]) > 0:
    print(a2[-1][0])