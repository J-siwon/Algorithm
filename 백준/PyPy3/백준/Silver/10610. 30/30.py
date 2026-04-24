import sys
input = sys.stdin.readline

t = list(input().strip())
isdone = False
for i in range(len(t)):
    if t[i] == "0":
        t.pop(i)
        isdone = True
        break

arrsum = 0
for i in t:
    arrsum += int(i)
if arrsum % 3 == 0 and isdone:
    ans = ""
    t.sort(reverse = True)
    for i in t:
        ans += i
    ans += "0"
    print(ans)
else:
    print(-1)