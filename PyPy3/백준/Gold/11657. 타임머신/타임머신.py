import sys
import math
import heapq
from collections import deque, Counter

def bellman_ford(start):
    # 시작 노드에 대해서 초기화
    d[start] = 0
    # 전체 v - 1번의 라운드(round)를 반복
    for i in range(n):
        # 매 반복마다 '모든 간선'을 확인한다.
        for j in range(m):
            cur_node = arr[j][0]
            next_node = arr[j][1]
            edge_cost = arr[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if d[cur_node] != int(1e9) and d[next_node] > d[cur_node] + edge_cost:
                d[next_node] = d[cur_node] + edge_cost
                # v번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1:
                    return True

    return False

n,m = map(int,input().split())
arr = []
for i in range(m):
    a,b,w = map(int, input().split())
    arr.append([a,b,w])

d = [int(1e9) for i in range(n+1)]

if bellman_ford(1):
    print(-1)
else:
    for i in range(2, n + 1):
        # 도달할 수 없는 경우, -1 출력
        if d[i] == int(1e9):
            print("-1")
        # 도달할 수 있으면 거리 출력
        else:
            print(d[i])