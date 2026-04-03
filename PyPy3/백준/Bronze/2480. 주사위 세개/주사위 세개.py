import sys
input = sys.stdin.readline

a, b, c = map(int, input().strip().split())

if(a==b):
    if(b==c):
        x = 10000 +  a * 1000
    else:
        x = 1000 + a * 100
else:
    if(b==c):
        x = 1000 +  b * 100
    elif(a==c):
        x = 1000 +  a * 100
    else:
        x = max(a, b, c) * 100

print(x)