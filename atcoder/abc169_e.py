# abc169_e.py
N = int(input())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
n = N-1
if N%2 ==1:
    print(B[(n+1)//2]-A[(n+1)//2])
else:
    print((B[n//2]+B[n//2+1])/2 - (A[n//2]+A[n//2+1])/2)
    print((B[n//2]+B[n//2+1])/2 , (A[n//2]+A[n//2+1])/2)
