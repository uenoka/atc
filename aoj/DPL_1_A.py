# DPL_1_A.py
N, M = map(int, input().split())
C = [0]
C += list(map(int, input().split()))
dp = [[0 for i in range(N+1)] for i in range(M+1)]
print(C)
for i in range(1, N):
    for j in range(1, M):
        if j < C[i]:
            dp[i][j] = dp[i-1][j]

print(dp[N][M])
