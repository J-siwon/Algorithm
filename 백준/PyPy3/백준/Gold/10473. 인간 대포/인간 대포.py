import sys
input = sys.stdin.readline

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

x,y = map(float, input().split())
dx, dy = map(float, input().split())
n = int(input())

point = []
point.append((x,y))
for i in range(n):
    a,b = map(float,input().split())
    point.append((a,b))

arr = [[1e9 for i in range(n+1)] for i in range(n+1)]

for i in range(n+1):
    arr[0][i] = dist(x,y,point[i][0], point[i][1]) / 5

for i in range(1,n+1):
    for j in range(n+1):
        d = dist(point[i][0], point[i][1], point[j][0], point[j][1])
        if d >= 50:
            arr[i][j] = (d - 50) / 5 + 2
        else:
            arr[i][j]  = min(d/5, (50-d)/5 + 2)

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

m = dist(x,y,dx,dy) / 5
for i in range(1, n+1):
    j = (dx,dy)
    d = dist(point[i][0], point[i][1], j[0], j[1])
    if d >= 50:
        m = min(m, (d - 50) / 5 + 2 +arr[0][i])
    else:
        m = min(m, min(d / 5, (50 - d) / 5 + 2) + arr[0][i])
print(m)