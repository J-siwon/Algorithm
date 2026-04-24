import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
b = set(a)

while(len(b) != 1 or b != {0}):
    
    if (sum(a) - max(a)) <= max(a):
        print("Invalid")
    elif(len(b) == 1):
        print("Equilateral")
    elif(len(b) == 2):
        print("Isosceles")
    else:
        print("Scalene")
    a = list(map(int, input().split()))
    b= set(a)