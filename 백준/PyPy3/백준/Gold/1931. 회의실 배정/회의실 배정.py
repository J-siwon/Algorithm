import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

arr = sorted(arr, key = lambda x:(x[0], x[1]))
count = 0
fin = 0
for i in arr:
    if i[0] >= fin:
        count+=1
        fin = i[1]
        continue
    fin = min(fin, i[1])
print(count)