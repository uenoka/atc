#abc132_b.py
def is_center(A,i):
    if (A[i-1]<A[i] and A[i]<A[i+1]) or (A[i-1]>A[i] and A[i]>A[i+1]):
        return True
    return False

N = int(input())
A = list(map(int,input().split()))
cnt = 0
for i in range(1,N-1):
    if is_center(A,i):
        cnt+= 1
print(cnt)