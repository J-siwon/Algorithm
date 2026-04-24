import sys
import math
input = sys.stdin.readline

times = int(input())
a = []
b = [0 ]* 8001
for i in range(times):
    x = int(input())
    a.append(x)
    b[x+4000] += 1

a = sorted(a)
print(round(sum(a) / len(a)))
print(a[(len(a)-1)//2])
maxb = 0
index = 0
issecond = 0
for i in range(len(b)):
    if b[i] > maxb:
        issecond = 0
        maxb = b[i]
        index = i
    elif b[i] == maxb:
        issecond +=1
        if issecond == 1:
            index = i
print(index-4000)
print(a[-1] - a[0])