import sys
input = sys.stdin.readline

p1 = int(input())
count = 0
x= 666

while count != p1:
    if "666" in str(x):
        count += 1
    x+= 1

print(x-1)