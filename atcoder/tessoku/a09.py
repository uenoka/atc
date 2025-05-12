H,W,N=map(int, input().split())
X=[[0 for _ in range(W+1)] for _ in range(H+1)]
for i in range(N):
    A,B,C,D=map(int, input().split())
    X[A][B] += 1
    X[C+1][D+1] += 1
    X[A][D+1] -= 1
    X[C+1][B] -= 1
ans = [[0 for _ in range(W+1)] for _ in range(H+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        ans[i][j] = X[i][j] + ans[i-1][j] + ans[i][j-1] - ans[i-1][j-1]
for i in range(1,H+1):
    for j in range(1,W+1):
        print(ans[i][j], end=' ')
    print()

