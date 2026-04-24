import sys
input = sys.stdin.readline

x = list(input())
while(x[0] != '.'):
    a = []
    isprinted = False
    for j in x:
        if j == "(":
            a.append("(")
        elif j == ")":
            if len(a) == 0 or a[-1] != "(":
                print("no")
                isprinted = True
                break
            else:
                a.pop()
        elif j == "[":
            a.append("[")
        elif j == "]":
            if len(a) == 0 or a[-1] != "[":
                print("no")
                isprinted = True
                break
            else:
                a.pop()
    if isprinted:
        x = list(input())
        continue
    if len(a)==0:
        print("yes")
    else:
        print("no")

    x = list(input())