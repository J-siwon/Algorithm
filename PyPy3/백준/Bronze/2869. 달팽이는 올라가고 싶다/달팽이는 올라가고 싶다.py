import sys
input = sys.stdin.readline

a,b,v= map(int, input().split())
up = a-b
times = 0

times+= (v - a) // up

if (v-a) % up ==0:
    times+=1
else:
    times+=2

if v-a <= 0:
    times = 1

print(times)