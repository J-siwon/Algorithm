a,b,c,d = map(int, input().split())

isdone = False
for i in range(300):
    for j in range(300):
        for k in range(300):
            if a*i + b*j + c*k == d:
                isdone = True


print(int(isdone))