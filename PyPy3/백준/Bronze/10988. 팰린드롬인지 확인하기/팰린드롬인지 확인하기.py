import sys
input= sys.stdin.readline

x = input().strip()

if(x[::-1] == x):
    print(1)
else:
    print(0)
