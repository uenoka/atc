# DPL_1_B.py

n, wmax = map(int, input().split())
V = [0]
W = [0]
for i in range(n):
    v, w = map(int, input().split())
    V.append(v)
    W.append(w)
# dp = [[0 for i in range(W+1)] for i in range(N+1)]
dp = [[0 for i in range(wmax+1)] for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, wmax+1):
        if j < W[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i]]+V[i])
# print(dp)
print(dp[n][wmax])
