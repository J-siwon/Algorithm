import sys
import math
from collections import deque
input = sys.stdin.readline


def BackTracking(num, ongoing):
    global minans
    global maxans
    global plus, minus, mul, div

    if len(num)== 0:
        minans = min(minans, ongoing)
        maxans = max(maxans, ongoing)
        return
    
    if plus >0:
        plus -= 1
        t = num.pop()
        ongoing += t
        BackTracking(num, ongoing)
        ongoing -= t
        plus += 1
        num.append(t)

    if minus >0:
        minus -= 1
        t = num.pop()
        ongoing -= t
        BackTracking(num, ongoing)
        ongoing += t
        minus +=1
        num.append(t)

    if mul >0:
        mul -=1
        t = num.pop()
        ongoing = ongoing * t
        BackTracking(num, ongoing)
        ongoing = ongoing // t
        mul += 1
        num.append(t)

    
    if div >0:
        div -=1
        temp = ongoing
        t = num.pop()
        if ongoing < 0:
            ongoing = -ongoing //t
            ongoing *= -1
        else:
            ongoing = ongoing // t
        BackTracking(num, ongoing)
        ongoing = temp
        div +=1
        num.append(t)
        

x= int(input())
num = list(map(int, input().split()))
num.reverse()
plus, minus, mul, div = map(int, input().split())

maxans = -1000000000
minans = 1000000000

t = num.pop()
BackTracking(num, t)
print(maxans)
print(minans)