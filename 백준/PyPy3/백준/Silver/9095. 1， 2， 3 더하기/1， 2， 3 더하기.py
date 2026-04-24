import sys
import math
from collections import deque
input = sys.stdin.readline


def Backtrack(temp):
    global count, ad
    if ad == temp:
        count +=1
        return
    elif ad > temp:
        return
    
    for i in t:
        ad += i
        Backtrack(temp)
        ad -= i

x = int(input())
t = [1,2,3]
for i in range(x):
    count = 0
    ad = 0
    temp = int(input())
    Backtrack(temp)
    print(count)

