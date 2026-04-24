import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

alpha = "abcdefghijklmnopqrstuvwxyz"

n = int(input())
for i in range(n):
    arr = []
    x = input().strip().lower()
    for j in alpha:
        if j not in x:
            arr.append(j)
    arr = sorted(arr)
    if len(arr) == 0:
        print("pangram", end ="")
    else:
        print("missing", end = " ")
        for j in arr:
            print(j, end= "")
    print()
