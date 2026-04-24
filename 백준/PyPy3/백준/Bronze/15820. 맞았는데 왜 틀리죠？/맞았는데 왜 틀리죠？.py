import sys
input= sys.stdin.readline

x, y = map(int, input().split())

ans = "Accepted"
for i in range(x):
    a, b = map(int, input().split())
    if a != b:
        ans = "Wrong Answer"

for i in range(y):
    a, b = map(int, input().split())
    if ans == "Accepted":
        if a != b:
            ans = "Why Wrong!!!"

print(ans)