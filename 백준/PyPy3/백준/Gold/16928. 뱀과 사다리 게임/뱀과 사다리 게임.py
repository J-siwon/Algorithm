import sys
import math
from collections import deque, Counter
sys.setrecursionlimit(2*10**5)

n,m = map(int, input().split())

ladder = []
snake = []

for i in range(n):
    ladder.append(list(map(int, input().split())))
for i in range(m):
    snake.append(list(map(int, input().split())))

count = 0

dice = [1,2,3,4,5,6]
tovisit = deque()
now = 1

iscon = False
visited = []
for i in dice:
    for j in ladder:
        if j[0] == now +i:
            tovisit.appendleft([j[1], count+1])
            visited.append(i)

    for j in snake:
        if j[0] == now + i:
            tovisit.appendleft([j[1], count + 1])
            visited.append(i)

reverseddice = [6,5,4,3,2,1]
for i in reverseddice:
    if i not in visited:
        tovisit.appendleft([now+i, count +1])
        break


while len(tovisit) > 0:
    t = tovisit.pop()
    now = t[0]
    count = t[1]
    if now >= 100:
        break

    visited = []
    for i in dice:
        for j in ladder:
            if j[0] == now + i:
                tovisit.appendleft([j[1], count + 1])
                visited.append(i)

        for j in snake:
            if j[0] == now + i:
                tovisit.appendleft([j[1], count + 1])
                visited.append(i)

    for i in reverseddice:
        if i not in visited:
            tovisit.appendleft([now + i, count + 1])
            break


print(count)