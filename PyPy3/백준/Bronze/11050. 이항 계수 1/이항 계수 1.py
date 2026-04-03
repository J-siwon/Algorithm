import sys
input = sys.stdin.readline

x,y = map(int,input().split())
a = 1
for i in range(1,y+1):
    a*= x
    x-=1

for i in range(y):
    a = a //y
    y-=1

print(a)