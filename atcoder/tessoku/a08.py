H,W = map(int, input().split())
X = [[0 for _ in range(W+1)] for _ in range(H+1)]

for i in range(1,H+1):
    Xi = [0] + list(map(int, input().split()))
    for j in range(1,W+1):
        X[i][j] = Xi[j] + X[i-1][j] + X[i][j-1] - X[i-1][j-1]
print(X)
for Q in range(int(input())):
    A,B,C,D = map(int, input().split())
    ans = X[C][D] - X[A-1][D] - X[C][B-1] + X[A-1][B-1]
    print(ans)