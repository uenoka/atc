# ALDS1_2_C.py
import copy


def bubbleSort(A, N):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(N-1):
            if A[i][0] > A[i+1][0]:
                tmp = A[i]
                A[i] = A[i+1]
                A[i+1] = tmp
                isSorted = False
    return A


def selectionSort(A, N):
    for i in range(N):
        minj = i
        for j in range(i+1, N):
            if A[j][0] < A[minj][0]:
                minj = j
        if minj != i:
            tmp = A[i]
            A[i] = A[minj]
            A[minj] = tmp
    return A


def join(A):
    ans = []
    for a, b in A:
        ans.append(b+a)
    return ans


N = int(input())
S = input().split()
bA = []
sA = []
for i in S:
    bA.append((i[1], i[0]))
    sA.append((i[1], i[0]))

bubbleSorted = bubbleSort(bA, N)
selectionSorted = selectionSort(sA, N)
bubbleSorted = join(bubbleSorted)
selectionSorted = join(selectionSorted)
print(*bubbleSorted)
print("Stable")
print(*selectionSorted)
isStable = True
for i in range(N):
    if bubbleSorted[i] != selectionSorted[i]:
        isStable = False
        break
print("Stable" if isStable else "Not stable")
