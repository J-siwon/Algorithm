import sys
import math
input = sys.stdin.readline

def factorial(i):
    if (i == 0):
        return 1
    else:
        return factorial(i-1) * i
    
print(factorial(int(input())))