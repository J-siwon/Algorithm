import sys
import math
from collections import deque
input = sys.stdin.readline

for r in range(int(input())):
    x = int(input())
    arr= list(map(int,input().split()))
    arr= sorted(arr)
    print(len(set(arr)))