import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

r,c = map(int, input().split())
score = list(map(int, input().split()))
num = []
for i in range(c):
    arr = list(input().split())
    t = 0
    for j in range(1,len(arr)):
        if arr[j]== "O":
            t+= int(score[j-1])
    num.append([int(arr[0]), t])

num = sorted(num, key= lambda x:(int(x[1]),-int(x[0])))
print(*num[-1])