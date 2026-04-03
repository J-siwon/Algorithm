import sys
import math
from collections import deque
input = sys.stdin.readline

for i in range(int(input())):
    x = int(input())
    print("Pairs for " + str(x), end=": ")

    arr =[]
    if x % 2 ==0:
        for j in range(1,x//2):
            arr.append([j,x-j])
    else:
        for j in range(1, x//2+1):
            arr.append([j, x-j])
    for j in range(len(arr)-1):
        print(*arr[j], end = ", ")
    
    if len(arr) > 0:
        print(*arr[-1])
    else:
        print()