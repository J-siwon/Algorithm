import sys
input = sys.stdin.readline

times, prob = map(int,input().split())
inputlist = dict()
inputlist2 = dict()
for i in range(1, times+1):
    x = input().strip()
    inputlist[x] = str(i)
    inputlist2[str(i)] = x

for i in range(prob):
    x = input().strip()
    if x in inputlist.keys():
        print(inputlist[x])
    if x in inputlist2.keys():
        print(inputlist2[x])