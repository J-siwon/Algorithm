import sys
input= sys.stdin.readline

x = int(input())
a= list()
while(x != -1):
    a = list()
    for i in range(1,x):
        if x % i == 0:
            a.append(i)

    ans = ""
    if sum(a) == x:
        ans = str(x) + " = 1"
        for i in a:
            if i == 1:
                continue
            ans = ans + " + " + str(i)
    else:
        ans = str(x) + " is NOT perfect."
    print(ans)
    x = int(input())