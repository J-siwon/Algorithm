import sys
input= sys.stdin.readline

time = int(input())
a = ""

for k in range(time):
    x, y = input().split()
    for i in y:
        for j in range(int(x)):
            a += i
    print(a)
    a = ""

