# abc129_c.py
N, M = map(int, input().split())
A = [0]
mod = 1000000007
for i in range(M):
    A.append(int(input()))
idx = 1
dp = [0]*(N+1)
dp[0] = 1
for i in range(1, N+1):
    if idx < len(A) and A[idx] == i:
        dp[i] = 0
        idx += 1
    else:
        if i < 2:
            dp[i] = dp[i-1] % mod
        else:
            dp[i] = (dp[i-1]+dp[i-2]) % mod
# print(dp)
print(dp[N])
