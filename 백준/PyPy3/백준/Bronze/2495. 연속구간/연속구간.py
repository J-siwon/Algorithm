for i in range(3):
    t = input().strip()
    b = -1
    c = 0
    maxc = 1
    for i in t:
        if b == i:
            c+=1
            maxc = max(c, maxc)
        else:
            b = i
            c = 1

    print(maxc)