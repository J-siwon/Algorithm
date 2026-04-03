import sys
input = sys.stdin.readline

times = int(input())
ra = set()
ra.add("ChongChong")
for i in range(times):
    x,y = input().split()
    if x in ra:
        if y not in ra:
            ra.add(y)
    else:
        if y in ra:
            ra.add(x)
print(len(ra))