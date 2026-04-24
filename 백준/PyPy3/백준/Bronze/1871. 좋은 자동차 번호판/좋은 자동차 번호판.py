n  = int(input())
for i in range(n):
    s = input().strip()
    a = (ord(s[0]) - ord('A'))* 26**2 + (ord(s[1]) - ord('A'))* 26**1 +(ord(s[2]) - ord('A'))
    if abs(a - int(s[4:])) <= 100:
        print("nice")
    else:
        print("not nice")