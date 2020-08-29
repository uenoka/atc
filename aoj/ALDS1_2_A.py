# ALDS1_2_A.py
def bubbleSort(A: list, N: int):
    cnt = 0
    isEnd = False
    while not isEnd:
        isEnd = True
        for i in range(1, N):
            if A[i] < A[i-1]:
                tmp = A[i]
                A[i] = A[i-1]
                A[i-1] = tmp
                isEnd = False
                cnt += 1
    return A, cnt


N = int(input())
A = list(map(int, input().split()))
A, cnt = bubbleSort(A, N)
print(*A)
print(cnt)
