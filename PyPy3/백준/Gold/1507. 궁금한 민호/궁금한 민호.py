import heapq
import sys
input = sys.stdin.readline

def dijk(startv):
    d = [1e9 for i in range(n)]
    q = [(0, startv)]

    while(len(q)>0):
        t = heapq.heappop(q)
        now = t[1]
        cost = t[0]

        if d[now] < cost:
            continue

        for i in arr[now]:
            if d[i[1]] > cost + i[0]:
                d[i[1]] = cost + i[0]
                heapq.heappush(q, (cost + i[0], i[1]))

    return d

n = int(input())
arr = [[] for i in range(n)]

road = []

for i in range(n):
    l = list(map(int, input().split()))
    for j in range(i+1,n):
        heapq.heappush(road, (l[j], i,j))

roadcount = 0
isdone = False
while(len(road) > 0):
    t = heapq.heappop(road)
    a = t[1]
    b = t[2]
    c = t[0]

    if dijk(a)[b] == c:
        continue

    if dijk(a)[b] < c:
        print(-1)
        isdone = True
        break

    arr[a].append((c,b))
    arr[b].append((c,a))
    roadcount+= c

if not isdone:
    print(roadcount)
