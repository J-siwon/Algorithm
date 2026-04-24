import sys
import math
from collections import deque
input = sys.stdin.readline

x = int(input())
arr = [0,0,1,1,2,3,2,3,3,2,3]
for i in range(11,x+1):
    ismin = min([arr[i-k] + k for k in range(1, 10)])

    if i%2==0:
        if i%3 ==0:
            toappend = min(arr[i//2]+1, arr[i//3]+1, ismin)
            arr.append(toappend)
        else:
            toappend = min(ismin, arr[i//2]+1)
            toappend = min(toappend, ismin)

            arr.append(toappend)
    else:
        if i%3 ==0:
            toappend = min(ismin, arr[i//3]+1)
            toappend = min(toappend, ismin)
            arr.append(toappend)
        else:
            arr.append(ismin)


print(arr[x])
    