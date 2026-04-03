import sys
input= sys.stdin.readline

x = int(input())

count = 0

alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(x):
    x = input().strip()
    a = [0] * 26

    group = True
    for j in range(len(x)):
        for k in range(26):
            if alpha[k] == x[j]:
                if a[k] == 1: #1은 발현됨
                    if j > 0:
                        if x[j] == x[j-1]:
                            break
                    group = False
                    a[k] = 2 #2는 중복됨
                elif a[k] == 0:
                    a[k] = 1
                    break
    if group:
        count += 1

print(count)