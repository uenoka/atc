# abc040_c.py
N = int(input())
A = [0] + list(map(int, input().split()))
INF = 10**9+7
dp = [INF] * (N+1)
dp[1] = 0
dp[2] = abs(A[1]-A[2])
for i in range(3, N+1):
    dp[i] = min(dp[i-1]+abs(A[i-1]-A[i]), dp[i-2]+abs(A[i-2]-A[i]))
print(dp[N])
