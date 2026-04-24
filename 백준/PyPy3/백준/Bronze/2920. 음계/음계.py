import sys
import math
from collections import deque
input = sys.stdin.readline

arr = list(map(int, input().split()))

ascending = True
descending = True
for i in range(1,len(arr)):
    if arr[i-1] > arr[i]:
        ascending = False
    if arr[i-1] < arr[i]:
        descending = False

if ascending == True:
    print("ascending")
elif descending == True:
    print("descending")
else:
    print("mixed")
