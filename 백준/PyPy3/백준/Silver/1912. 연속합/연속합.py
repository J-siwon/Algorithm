import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
arr = list(map(int, input().split()))
maxsum = 0
aftersum = 0
allsum = 0
for i in range(x):
    if i == 0:
        maxsum = arr[0]

    if arr[i] <=0:
        if allsum <= 0:
            maxsum = max(maxsum, arr[i])
            continue
        
        if allsum > aftersum:
            maxsum = max(maxsum, allsum)
            allsum += arr[i]
            aftersum = 0
        else:
            maxsum = max(maxsum, aftersum)
            allsum = aftersum + arr[i]
            aftersum = 0
    else:
        allsum += arr[i]
        aftersum += arr[i]

if allsum >0:
    maxsum = max(maxsum, aftersum, allsum)
    
print(maxsum)