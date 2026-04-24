import sys
input = sys.stdin.readline

times = int(input())
a = list(map(int,input().split()))
a = sorted(a)
print(a[0] * a[-1])
