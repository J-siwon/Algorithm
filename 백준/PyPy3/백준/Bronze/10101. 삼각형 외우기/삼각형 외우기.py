import sys
input = sys.stdin.readline

a= []
for i in range(3):
    x = int(input())
    a.append(x)

if sum(a) == 180:
    if len(set(a)) == 1:
        print("Equilateral")
    elif len(set(a)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
