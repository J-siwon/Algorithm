import sys
input= sys.stdin.readline

x = input().upper()
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = [0] *26

for i in x:
    for j in range(len(alpha)):
        if i == alpha[j]:
            a[j] += 1

max = max(a)
index = -1
for i in range(len(a)):
    if max == a[i]:
        if index == -1:
            index = i
        else:
            index = -1
            print("?")
            break

if index != -1:
    print(alpha[index])
