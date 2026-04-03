import sys
import math
from collections import deque
input = sys.stdin.readline

def BackTracking(put, col):
    if col == x:
        ans.append(put)
        return
    
    for i in range(x):
        if Check(col, i):
            put.append([col,i])
            BackTracking(put,col+1)
            put.pop()

def Check(a, b):
    for i in put:
        if a == i[0] or b == i[1]:
            return False
        
        if a-i[0] == b-i[1]:
            return False
        
        if i[0] - a == b-i[1]:
            return False
    return True


x = int(input())
put = []
ans = []
col = 0
BackTracking(put, col)
print(len(ans))