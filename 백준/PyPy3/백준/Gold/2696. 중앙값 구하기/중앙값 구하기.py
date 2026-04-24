import sys
import math
import heapq
from collections import deque, Counter
input = sys.stdin.readline

n = int(input())

for i in range(n):
    l = int(input())
    h = []
    heapq.heapify(h)
    x = []
    while(len(x) != l):
        for j in map(int, input().split()):
            x.append(j)

    t = []
    printcount = 0
    arr =[]
    for j in range(len(x)):
        if j % 2== 0:
            heapq.heappush(h, x[j])
            for k in range(j//2+1):
                t.append(heapq.heappop(h))
            arr.append(t[-1])
            for k in range(len(t)):
                heapq.heappush(h, t.pop())
        else:
            heapq.heappush(h,x[j])

    print(len(arr))
    for j in arr:
        print(j, end = " ")
        printcount += 1
        if printcount == 10:
            print()
            printcount = 0
    print()
