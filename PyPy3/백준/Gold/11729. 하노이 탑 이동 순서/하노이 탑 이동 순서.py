import sys
import math
from collections import deque
input = sys.stdin.readline

global a1
global a2
global a3
global ans

def Put(start, fin):
    ans.append(str(start[1]) + " " + str(fin[1]))
    fin[0].append(start[0].pop())


def Move(start, fin, count):
    
    lst = [a1,a2,a3]
    if(count ==1):
        Put(start, fin)
        return

    lst.remove(start)

    if count % 2 ==0:
        loc = lst.index(fin)-1
    else:
        loc = lst.index(fin)

    
    Put(start, lst[loc])
    for i in range(1, count):
        Put(start, lst[(loc+1) %2])
        Move(lst[loc], lst[(loc+1) %2], i)
        loc+=1
        loc = loc % 2

x = int(input())
a1 = ([i for i in range(x,0,-1)],1)
a2 = ([],2)
a3 = ([],3)
ans = []
Move(a1,a3,x)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
