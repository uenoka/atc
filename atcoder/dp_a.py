
# dp_a.py
'''
動的計画法の基礎問題
カエルはHi -> Hi+1 or Hi+2 に飛ぶので、どっちから来たらよりHiでのコストが低くなるかを計算していく
'''
N = int(input())
H = list(map(int, input().split()))
dp = [0]*N
for i in range(1, N):
    if i > 1:
        dp[i] = min(dp[i-1] + abs(H[i]-H[i-1]), dp[i-2] + abs(H[i]-H[i-2]))
    else:
        dp[i] = dp[i-1] + abs(H[i]-H[i-1])
print(dp[N-1])
