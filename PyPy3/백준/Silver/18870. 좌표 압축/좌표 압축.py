import sys
input = sys.stdin.readline

#정렬 -> 순서를 튜플로 부여 
x = int(input())
inputlist = list(map(int, input().split()))
a =[]
#a = [입력값배열, 인덱스]
for i in range(x):
    a.append([inputlist[i], i])

#a를 배열 크기별로 정렬
a = sorted(a, key= lambda t: t[0])
b = sorted(inputlist)
count = 0
a[0][0] = 0
for i in range(1,x):
    if a[i][0] == b[i-1]:
        a[i][0] = count
    else:
        count+=1
        a[i][0] = count
        
a = sorted(a, key = lambda t: t[1])
for i in a:
    print(i[0], end = " ")
