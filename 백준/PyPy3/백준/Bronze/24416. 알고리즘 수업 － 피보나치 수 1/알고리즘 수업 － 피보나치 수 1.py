import sys
import math
from collections import deque
input = sys.stdin.readline

def fib(n):
    global count1
    
    if n==1 or n==2:
        count1 +=1
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fib2(n):
    global count2
    arr[0] = 1
    arr[1] = 1
    for i in range(2,n):
        arr[i] = arr[i-1] + arr[i-2]
        count2+=1
    return arr[n-1]
    

count1 = 0
count2 = 0
x = int(input())
arr = [0]* x
fib(x)
fib2(x)
print(count1, end=" ")
print(count2)