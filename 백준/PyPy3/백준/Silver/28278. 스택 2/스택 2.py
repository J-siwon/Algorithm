import sys
input = sys.stdin.readline

x = int(input())
a = []
for i in range(x):
    inp = list(map(int, input().split()))
    if len(inp) == 2:
        if inp[0] == 1:
            a.append(inp[1])
    else:
        if inp[0] == 2:
            if len(a) == 0:
                print(-1)
            else:
                print(a.pop())
        elif inp[0] == 3:
            print(len(a))
        elif inp[0] == 4:
            if len(a) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(a) == 0:
                print(-1)
            else:
                print(a[-1])
