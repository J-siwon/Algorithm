import sys
input= sys.stdin.readline


x = int(input())
max = 0
level = 1
while (max < x):
    max += level
    level += 1

index = x - (max - level + 1)
a = ""
if(level % 2 == 0):
    a = str(level-index) + "/" + str(index)
else:
    a = str(index) + "/" + str(level-index)
print(a)