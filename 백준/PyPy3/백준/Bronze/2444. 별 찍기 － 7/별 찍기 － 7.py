import sys
input= sys.stdin.readline

x = int(input())

for i in range(x):
    a = ""
    for j in range(x-i-1):
        a+= " "
    for j in range(2*i+1):
        a+= "*"
    print(a)

for i in range(1, x):
    a = ""
    for j in range(i):
        a+= " "
    for j in range(2*(x-i)-1):
        a+= "*"
    print(a)
