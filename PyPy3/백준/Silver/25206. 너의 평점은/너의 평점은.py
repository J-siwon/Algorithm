import sys
input= sys.stdin.readline

totaltime = 0
totalscore = 0
s = 0
for i in range(20):
    name, t, score = input().strip().split()
    t = float(t)

    for i in score:
        if i in "ABCD":
            if i =="A":
                s = 4.0
            elif i =="B":
                s = 3.0
            elif i == "C":
                s = 2.0
            else:
                s= 1.0
        elif i in "+0":
            if i == "+":
                s += 0.5
        elif i in "PF":
            if i == "P":
                t = 0
            else:
                s = 0

    totaltime += t
    totalscore += t * s

print(totalscore / totaltime)