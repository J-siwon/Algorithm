import sys
input = sys.stdin.readline

x = int(input())
a=1
for i in range(1,x+1):
    a*=i
print(a)