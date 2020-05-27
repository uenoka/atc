# hitachi2020_b.py
_, _, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
X = []
Y = []
C = []
amin = min(A)
bmin = min(B)
for i in range(M):
    x, y, c = map(int, input().split())
    X.append(x)
    Y.append(y)
    C.append(c)

ans = amin+bmin
for i in range(M):
    if ans >= A[X[i]-1]+B[Y[i]-1]-C[i]:
        ans = A[X[i]-1]+B[Y[i]-1]-C[i]
print(ans)
