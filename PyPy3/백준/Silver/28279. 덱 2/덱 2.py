import sys
from collections import deque
input = sys.stdin.readline

x = int(input())
a = deque()
for i in range(x):
    inputlist = list(map(int, input().split()))
    if inputlist[0] == 1:
        a.appendleft(inputlist[1])
    elif inputlist[0] == 2:
        a.append(inputlist[1])
    elif inputlist[0] == 3:
        if len(a) == 0:
            print(-1)
        else:
            print(a.popleft())
    elif inputlist[0] == 4:
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop())
    elif inputlist[0] == 5:
        print(len(a))
    elif inputlist[0] == 6:
        if len(a) == 0:
            print(1)
        else:
            print(0)
    elif inputlist[0] == 7:
        if len(a) == 0:
            print(-1)
        else:
            print(a[0])
    elif inputlist[0] == 8:
        if len(a) == 0:
            print(-1)
        else:
            print(a[-1])