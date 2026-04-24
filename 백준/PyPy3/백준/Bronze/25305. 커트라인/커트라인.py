import sys
input = sys.stdin.readline

x,y = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
print(a[-y])