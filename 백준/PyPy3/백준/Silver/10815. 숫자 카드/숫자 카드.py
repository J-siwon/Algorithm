import sys
input = sys.stdin.readline

x = int(input())
arr = set(map(int, input().split()))

x = int(input())
arr2 = list(map(int, input().split()))

dif = list(set(arr2).difference(arr))
inter = list(set(arr2).intersection(arr))

difdic = {dif[i]: 0 for i in range(len(dif))}
interdic = {inter[i]: 1 for i in range(len(inter))}
difdic.update(interdic)
for i in arr2:
    print(difdic[i], end = " ")