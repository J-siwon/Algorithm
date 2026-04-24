import sys
input = sys.stdin.readline

x, y = map(int, input().split())
set1 = set()
set2 = set()
for i in range(x):
    set1.add(input().strip())
for i in range(y):
    set2.add(input().strip())

inter = set1.intersection(set2)
inter = sorted(inter)
print(len(inter))
for i in inter:
    print(i)