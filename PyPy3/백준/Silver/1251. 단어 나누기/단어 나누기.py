s = input().strip()
arr= []
for i in range(1,len(s)-1):
    for j in range(i+1,len(s)):
        a = s[0:i]
        b= s[i:j]
        c = s[j::]
        arr.append(a[::-1] + b[::-1] + c[::-1])
arr = sorted(arr)
print(arr[0])