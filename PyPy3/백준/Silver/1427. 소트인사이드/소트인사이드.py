import sys
input = sys.stdin.readline

x = input().strip()

a = sorted(x)
ans = ""
for i in range(len(a)-1,-1, -1):
    ans += a[i]
print(ans)