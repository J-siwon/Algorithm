import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

a,b = input().split()
arr= set()
for i in range(int(a)):
    arr.add(input().strip())

if b == "Y":
    print(len(arr) // 1)
elif b == "F":
    print(len(arr) // 2)
elif b == "O":
    print(len(arr) // 3)