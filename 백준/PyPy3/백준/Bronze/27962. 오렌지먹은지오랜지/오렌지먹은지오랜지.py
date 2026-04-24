import sys
import math
from collections import deque, Counter

n = int(input())
s= input().strip()
isdone = False

for i in range(1,len(s)):
    a = s[:i]
    b = s[len(s)-i:]

    isdiff = False
    con = False
    for j in range(i):
        if a[j] != b[j]:
            if isdiff:
                con = True
                break
            else:
                isdiff = True

    if con:
        continue

    if isdiff and not con:
        isdone = True
        break
if isdone:
    print("YES")
else:
    print("NO")