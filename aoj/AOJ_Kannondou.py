# AOJ_Kannondou.py
import math
while True:
    N = int(input())
    if N == 0:
        break
    dp = [0]*(N+1)
    dp[0] = 1
    dp[1] = 1
    if N > 1:
        dp[2] = 2
    for i in range(3, N+1):
        dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
    # print(dp)
    print(math.ceil(math.ceil(dp[N]/10) / 365))
