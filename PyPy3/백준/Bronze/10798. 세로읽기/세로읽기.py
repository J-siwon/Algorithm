import sys
input = sys.stdin.readline

x = [0]* 5
for i in range(5):
    x[i] = input().strip()

a = ""

for j in range(15):
    for i in range(5):
        if(len(x[i]) <= j):
            continue
        a += x[i][j]

print(a)