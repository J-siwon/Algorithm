import sys
input = sys.stdin.readline

a, b = map(int, input().strip().split())

if(b<45):
    if(a == 0):
        a = 24
    print(str(a-1)+ ' ' + str(b+60-45))
else:
    print(str(a) + ' ' + str(b-45))