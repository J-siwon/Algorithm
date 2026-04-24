import sys
input = sys.stdin.readline

x= int(input())
back = 2
a = 0
for i in range(1, x+1):
    a = (back-1)*2 +1
    back = a
print(a**2)