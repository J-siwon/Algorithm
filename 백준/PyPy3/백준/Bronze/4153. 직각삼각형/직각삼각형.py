import sys
import math
from collections import deque
input = sys.stdin.readline

a,b,c= map(int, input().split())
arr= [a,b,c]
arr = sorted(arr)

while(a!=0 or b!=0 or c!=0):
    arr= [a,b,c]
    arr = sorted(arr)
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        print("right")
    else:
        print("wrong")
    a,b,c= map(int, input().split())