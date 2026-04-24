import sys
import math
from collections import deque, Counter
input = sys.stdin.readline

def Pow(a,b,c):
    if b== 1:
        return a % c
    if b%2==0:
        t = b//2
        return Pow(a,t,c)**2 % c
    else:
        t= (b-1)//2
        return (Pow(a,t,c)**2 * a) %c

a,b,c = map(int,input().split())
print(Pow(a,b,c)%c)