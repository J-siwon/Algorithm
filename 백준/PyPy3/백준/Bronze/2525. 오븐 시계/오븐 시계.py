import sys
input = sys.stdin.readline

a, b = map(int, input().strip().split())
c = int(input())

b = b+c
x = b// 60
if(x > 0):
    if(a + x >23):
        a = a - 24
    print(str(a + x)+ ' ' + str(b % 60))
else:
    print(str(a + x) + ' ' + str(b % 60))