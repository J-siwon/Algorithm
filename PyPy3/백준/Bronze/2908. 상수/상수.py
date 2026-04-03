import sys
input= sys.stdin.readline

a, b = input().split()

if(a[::-1] < b[::-1]):
    print(b[::-1])
else:
    print(a[::-1])
