import sys
input= sys.stdin.readline

alpha = "WelcomeToSMUPC"
x = int(input())

while(x > len(alpha)):
    x -= len(alpha)

print(alpha[x-1])