import sys
input = sys.stdin.readline

x = int(input())

a = list(map(int, input().split()))

print(str(min(a)) + " " + str(max(a)))