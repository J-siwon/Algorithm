import sys
input = sys.stdin.readline

x = int(input())
a = ""
b = 1
for b in range(1,x+1):
    a = ""
    for i in range(b, x):
        a += " "
    for j in range(x - b, x):
        a += "*"
    print(a)