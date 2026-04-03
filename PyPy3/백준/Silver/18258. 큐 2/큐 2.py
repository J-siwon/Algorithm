import sys
from collections import deque
input = sys.stdin.readline

x = int(input())
a = deque()
for i in range(x):
    inputlist = input().split()
    if inputlist[0] == "push":
        a.append(inputlist[1])
    elif inputlist[0] == "pop":
        if(len(a) == 0):
            print(-1)
        else:
            print(a.popleft())
    elif inputlist[0] == "size":
        print(len(a))
    elif inputlist[0] == "empty":
        if len(a) == 0:
            print(1)
        else:
            print(0)
    elif inputlist[0] == "front":
        if(len(a) == 0):
            print(-1)
        else:
            print(a[0])    
    elif inputlist[0] == "back":
        if(len(a) == 0):
            print(-1)
        else:
            b = a
            print(a[-1])