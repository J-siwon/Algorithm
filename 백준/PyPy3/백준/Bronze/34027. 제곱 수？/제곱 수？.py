n = int(input())
for i in range(1, n+1):
    t = int(input())
    a = int(t**(1/2))
    if a**2 == t:
        print(1)
    else:
        print(0)