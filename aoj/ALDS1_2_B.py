# ALDS1_2_B.py
def selectionSort(A,N):
    cnt=0
    for i in range(N):
        minj = i
        for j in range(i+1,N):
            if A[j] < A[minj]:
                minj = j
        if minj != i:
            tmp = A[i] 
            A[i] = A[minj]
            A[minj] = tmp
            cnt += 1
    return A,cnt
N = int(input())
A = list(map(int,input().split()))
A,cnt = selectionSort(A,N)
print(*A)
print(cnt)

