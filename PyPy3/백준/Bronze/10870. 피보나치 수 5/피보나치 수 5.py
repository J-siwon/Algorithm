import sys
import math
input = sys.stdin.readline

def fibo(n):
    if(n == 0):
        return 0
    elif(n == 1 or n==2):
        return 1
    
    return fibo(n-2) + fibo(n-1)

print(fibo(int(input())))