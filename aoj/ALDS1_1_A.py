# ALDS1_1_A.py
def insertionSort(a,n):
    for i in range(N):
        v = a[i]
        j = i-1
        while j>=0 and a[j]>v:
            a[j+1]=A[j]
            j-=1
        a[j+1] = v
        print(" ".join([str(_) for _ in a]))
N = int(input())
A = list(map(int,input().split()))
insertionSort(A,N)