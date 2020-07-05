# dp_b.py
def chmin(h, k, i):
    if i == 0:
        return 0
    ans = 10**9
    for j in range(min(i, k)):
        _min = dp[i-j-1] + abs(h[i]-h[i-j-1])
        if ans > _min:
            ans = _min
    return ans


N, K = map(int, input().split())
H = list(map(int, input().split()))
dp = [0]*N
for i in range(N):
    dp[i] = chmin(H, K, i)
    # print(dp)
print(dp[N-1])
