import sys
input = sys.stdin.readline

x, y = map(int, input().split())
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

print(len(set1.difference(set2)) + len(set2.difference(set1)))