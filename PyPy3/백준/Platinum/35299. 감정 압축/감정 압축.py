import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

s = input().strip()
arr = list(s[1:].split(":"))
k = int(input())

for i in range(len(arr)):
    if arr[i] == "(":
        arr[i] = 1
    else:
        arr[i] = 0

t0 = [0,0,0]
s0 = False
ou = False
t1 = [0,0,0]
s1 = False
zu = False
ans = [0,0,0,0,0]# index, 길이, 전환길이, 시작index, 다수
for i in range(len(arr)):
    if arr[i] == 0:
        s0 = True
        t0[0] += 1

        if t0[1] > 0:
            ou = True

        if zu:
            if t1[0] > ans[1] and t1[1] <= k:
                ans[0] = i
                ans[1] = t1[0]
                ans[2] = t1[1]
                ans[3] = t1[2]
                ans[4] = 1

            t1 = [0,0,i]
            zu = False
        else:
            t1[0] += 1
            t1[1] += 1
    else:
        t1[0] += 1

        if t1[1] > 0:
            zu = True

        if ou:
            if t0[0] > ans[1] and t0[1] <= k:
                ans[0] = i
                ans[1] = t0[0]
                ans[2] = t0[1]
                ans[3] = t0[2]
                ans[4] = 0

            t0 = [0,0,i]
            ou = False
        else:
            t0[0] += 1
            t0[1] += 1

if t1[1] > 0:
    if t1[0] > ans[1] and t1[1] <= k:
        ans[0] = len(arr)
        ans[1] = t1[0]
        ans[2] = t1[1]
        ans[3] = t1[2]
        ans[4] = 1

if t0[1] > 0:
    if t0[0] > ans[1] and t0[1] <= k:
        ans[0] = len(arr)
        ans[1] = t0[0]
        ans[2] = t0[1]
        ans[3] = t0[2]
        ans[4] = 0

for i in range(ans[3], ans[0]):
    arr[i] = ans[4]

writing = 2
c= 1
cs = ""
for i in arr:
    if i == 0:
        if writing == 0:
            c += 1
        else:
            if c>1:
                cs += str(c)
            cs += ":)"
            writing = 0
            c = 1
    else:
        if writing == 1:
            c += 1
        else:
            if c>1:
                cs += str(c)
            cs += ":("
            writing = 1
            c = 1

if c>1:
    cs += str(c)

print(len(cs))