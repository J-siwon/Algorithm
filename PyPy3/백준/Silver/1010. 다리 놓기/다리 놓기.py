import sys
input = sys.stdin.readline

times = int(input())
for i in range(times):
    x,y = map(int,input().split())
    a =1
    for j in range(x):
        a*= y
        y-=1
    for j in range(x):
        a = a // x
        x-=1
    print(a)