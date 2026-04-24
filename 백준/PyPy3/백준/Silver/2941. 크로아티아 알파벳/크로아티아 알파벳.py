import sys
input= sys.stdin.readline

x = input().strip()

count = 0
i = 0
while(i < len(x)-1):
    if x[i] == 'c':
        if x[i+1] == '=' or x[i+1] == '-':
            i += 2
            count += 1
        else:
            i += 1
            count += 1
    elif x[i] == 'd':
        if x[i+1] == 'z' and i+2 < len(x):
            if x[i+2] == '=':
                i += 3
                count += 1
            else:
                i += 1
                count += 1
        elif x[i+1] == '-':
            i += 2
            count += 1
        else:
            i += 1
            count+= 1
    elif x[i] == 'l' and x[i+1] == 'j':
        i += 2
        count +=1
    elif x[i] == 'n' and x[i+1] == 'j':
        i += 2
        count +=1
    elif x[i] == 's' and x[i+1] == '=':
        i += 2
        count +=1
    elif x[i] == 'z' and x[i+1] == '=':
        i += 2
        count +=1
    else:
        i+= 1
        count +=1

if(i == len(x)-1):
    count += 1

print(count)