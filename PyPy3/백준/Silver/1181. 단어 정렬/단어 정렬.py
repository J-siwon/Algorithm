import sys
input= sys.stdin.readline


x = int(input())
words = set()
for i in range(x):
    inputstring = input().strip()
    words.add(inputstring)

sortedlist = sorted(list(words))

for i in range(51):
    for j in sortedlist:
        if len(j) == i:
            print(j)