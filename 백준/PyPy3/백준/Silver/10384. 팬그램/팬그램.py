import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(n):
    s = input().strip().lower()
    c = Counter(s)
    minl = 1e9
    for j in alpha:
        if j in c:
            minl = min(minl, c[j])
        else:
            minl = 0
            break

    if minl >= 3:
        print("Case " + str(i+1) + ": "+ "Triple pangram!!!")
    elif minl >= 2:
        print("Case " + str(i+1) + ": "+ "Double pangram!!")
    elif minl >= 1:
        print("Case " + str(i+1) + ": "+ "Pangram!")
    else:
        print("Case " + str(i+1) + ": "+ "Not a pangram")