import sys
input = sys.stdin.readline

times = int(input())
inputlist = []
for i in range(times):
    x, y = input().split()
    inputlist.append([x,y])

p = []

for i in range(len(inputlist)):
    if inputlist[i][1] == "enter":
        p.append(inputlist[i][0])
    else:
        p.remove(inputlist[i][0])

p = sorted(p)
for i in range(len(p)-1,-1, -1):
    print(p[i])