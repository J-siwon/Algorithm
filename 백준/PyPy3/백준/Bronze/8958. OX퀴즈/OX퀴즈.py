import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
for i in range(x):
    arr = input().strip()
    score = 0
    get = 0
    if arr[0] == "O":
        get +=1
        score += get
    for i in range(1,len(arr)):
        if arr[i] == "O":
            get += 1
            score += get
        if arr[i] == "X":
            get = 0

    print(score)
