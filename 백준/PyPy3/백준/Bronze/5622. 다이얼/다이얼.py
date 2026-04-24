import sys
input= sys.stdin.readline

a = input()


sum =0
for i in a:
    for j in "ABC":
        if(i == j):
            sum += 3
            break
    for j in "DEF":
        if(i == j):
            sum += 4
            break
    for j in "GHI":
        if(i == j):
            sum += 5
            break
    for j in "JKL":
        if(i == j):
            sum += 6
            break
    for j in "MNO":
        if(i == j):
            sum += 7
    for j in "PQRS":
        if(i == j):
            sum += 8
            break
    for j in "TUV":
        if(i == j):
            sum += 9
            break
    for j in "WXYZ":
        if(i == j):
            sum += 10
            break

    
print(sum)
