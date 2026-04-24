import sys
input = sys.stdin.readline

x = int(input())
for i in range(x):
    xx = list(input().strip())
    a = []
    isprinted = False
    for j in xx:
        if j == "(":
            a.append(0)
        else:
            if len(a) == 0:
                print("NO")
                isprinted = True
                break
            else:
                a.pop()
    if isprinted:
        continue
    if len(a)==0:
        print("YES")
    else:
        print("NO")
