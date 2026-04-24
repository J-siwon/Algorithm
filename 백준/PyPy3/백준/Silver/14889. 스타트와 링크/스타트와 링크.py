import sys
import math
from collections import deque
input = sys.stdin.readline


def BackTracking(arr, player):
    global teamA
    global teamB
    global teamdif

    if len(player) == 0:
        if abs(teamB-teamA) < teamdif:
            teamdif = abs(teamB-teamA)
        return

    if len(Aplayer) < x//2:
        t = player.pop()
        origin = teamA
        for i in Aplayer:
            teamA += arr[t][i]
            teamA += arr[i][t]
        Aplayer.append(t)
        BackTracking(arr, player)
        player.append(t)
        Aplayer.pop()
        teamA = origin
    
    if len(Bplayer) < x//2:
        t = player.pop()
        origin = teamB
        for i in Bplayer:
            teamB += arr[t][i]
            teamB += arr[i][t]
        Bplayer.append(t)
        BackTracking(arr, player)
        player.append(t)
        Bplayer.pop()
        teamB = origin

x = int(input())
arr = []
for i in range(x):
    arr.append(list(map(int,input().split())))

player = [i for i in range(x)]
Aplayer = []
Bplayer = []

teamA = 0
teamB = 0
teamdif = 1000000000000
BackTracking(arr, player)
print(teamdif)