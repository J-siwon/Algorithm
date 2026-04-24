c = 0
n = int(input())
t = n
while(n >= 5):
    c+=1
    n -= 5
if t > 5 and n % 2 == 1:
    c -=1
    n += 5
while(n >= 2):
    c += 1
    n -= 2

if n == 1:
    print(-1)
else:
    print(c)