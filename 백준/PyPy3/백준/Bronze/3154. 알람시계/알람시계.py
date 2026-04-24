import sys
import math
from collections import deque, Counter

def effort(x,y):
    arr = [[4,2], [1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]]
    t1 = x//10
    t2 = x%10
    t3 = y//10
    t4 = y%10
    return abs(arr[t2][0] - arr[t1][0]) + abs(arr[t2][1] - arr[t1][1]) + abs(arr[t3][0] - arr[t2][0]) + abs(arr[t3][1] - arr[t2][1]) + abs(arr[t4][0] - arr[t3][0]) + abs(arr[t4][1] - arr[t3][1])
a,b = map(int, input().split(':'))
count = effort(a,b)
ans = [a,b]

while(a < 100):
    bc = 0
    while(b < 100):
        if count > effort(a,b):
            ans = [a,b]
            count = effort(a,b)
        b+=60
        bc += 1
    a+= 24
    b-= 60 * bc
if ans[0] < 10:
    print("0", end = "")
print(ans[0], end = ":")
if ans[1] < 10:
    print("0", end = "")
print(ans[1])