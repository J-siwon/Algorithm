import sys
import math
input = sys.stdin.readline


lst = []
def merge_sort(A, p, r) :
    if (p < r):
        q = (p + r) // 2;       # q는 p, r의 중간 지점
        merge_sort(A, p, q);      # 전반부 정렬
        merge_sort(A, q + 1, r);  # 후반부 정렬
        merge(A, p, q, r);        # 병합
    


# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(A, p, q, r) :
    i = p
    j =q + 1
    t = 0
    tmp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i+=1
        else:
            tmp.append(A[j])
            j+=1 # tmp[t] <- A[j]; t++; j++;
    
    while (i <= q) : # 왼쪽 배열 부분이 남은 경우
        tmp.append(A[i])
        i += 1
    while (j <= r) : 
        tmp.append(A[j])
        j+=1
    i = p
    t = 0
    while (i <= r) :
        A[i] = tmp[t]
        lst.append(tmp[t])
        i+= 1
        t +=1
        


x, y = map(int, input().split())
arr  =list(map(int, input().split()))
merge_sort(arr, 0, len(arr)-1)

if(y > len(lst)):
    print(-1)
else:
    print(lst[y-1])