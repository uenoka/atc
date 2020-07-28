# ALDS1_2_C.py

def bubbleSort(A,N):
    isSorted = False
    while not isSorted:
        isSorted=True
        for i in range(N-1):
            if A[i]>A[i+1]:
                tmp = A[i]
                A[i]=A[i+1]
                A[i+1]=tmp
                isSorted=False
    return A

def selectionSort(A,N):
    for i in range(N):
        minj = i
        for j in range(i+1,N):
            if A[j] < A[minj]:
                minj = j
        if minj != i:
            tmp = A[i] 
            A[i] = A[minj]
            A[minj] = tmp
    return A


N = int(input())
S = input().split()
A = list(map(int,input().split()))
print(bubbleSort(A,N))
print(selectionSort(A,N))
