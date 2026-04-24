import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

def dijk(arr, startv):
    d= [1e9 for i in range(n)]
    d[startv-1] = 0

    q = []
    heapq.heappush(q,(0,startv))

    while(len(q) > 0):
        t = heapq.heappop(q)
        cost = t[0]
        dest = t[1]
        if d[dest-1] < cost:
            continue

        for i in arr[dest-1]:
            if d[i[1]-1] < 0:
                continue

            if d[i[1]-1] > cost + i[0]:
                d[i[1] - 1] = cost + i[0]
                heapq.heappush(q, (cost + i[0], i[1]))

    return d



times = int(input())
for time in range(times):
    n,m,w = map(int, input().split())
    arr = [[] for _ in range(n)]
    check = []
    for i in range(m):
        a,b,c = map(int, input().split())
        arr[a-1].append((c,b))
        arr[b-1].append((c,a))

    isdone = False
    for i in range(w):
        a, b, c = map(int, input().split())
        arr[a-1].append((-c,b))
        check.append((a,b))


    for i in range(n):
        d1 = dijk(arr, i + 1)
        if d1[i] < 0:
            isdone = True
            print("YES")
            break

    if not isdone:
        print("NO")