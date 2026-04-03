import sys
import math
input = sys.stdin.readline

x = int(input())

#a는 가로수 위치 배열
a = []
for i in range(x):
    a.append(int(input()))

#a는 가로수간 거리 배열
length = []
for i in range(1, len(a)):
    length.append(a[i] - a[i-1])

#q는 첫번째 가로수간 거리의 약수 배열
q = []
for i in range(1, math.floor(length[0] **(1/2)) +1+1):
    if length[0] % i ==0:
        q.append(i)
        q.append(length[0] // i)

#result는 특정 거리로 했을 때 가로수 개수 배열
result = []
#sum은 특정 거리로 했을 때 가로수 개수
sum = 0

for j in q:
    sum = 0
    for i in length:
        if i % j !=0:
            sum = 0
            break
        else:
            sum += i // j -1
    if sum != 0:
        result.append(sum)

if(len(set(length)) == 1):
    result.append(0)

print(min(result))