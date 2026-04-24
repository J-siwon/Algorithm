import sys
input= sys.stdin.readline

x = input()
count = 0
for i in x:
    if i == "7":
        count = 2

if int(x) % 7 == 0:
    count += 1

print(count)