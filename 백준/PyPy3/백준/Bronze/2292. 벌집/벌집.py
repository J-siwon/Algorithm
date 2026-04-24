import sys
input = sys.stdin.readline

x= int(input())
i = 2
a = 0
times = 1
while(i<=x):
    a += 6
    i += a
    times += 1

print(times)