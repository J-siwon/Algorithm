import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
ansx = 0
ansy = 0
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if(a[0] * i + a[1] * j == a[2] and a[3] * i + a[4] * j == a[5]):
            ansx = i
            ansy = j
            break
    
    if ansx != 0:
        break

ans = str(ansx) + " " + str(ansy)
print(ans)