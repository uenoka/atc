# dp_i.py
'''
解説読んで何とか分かった気がするという感じ。
何となくのイメージは出来たけど、これを空で問題解けって言われたらなにもできずだなぁ。。。
'''


def printdp():
    for i in dp:
        print(i)


N = int(input())
P = [0]
P += list(map(float, input().split()))
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(i+1):
        if j > 0:
            dp[i][j] = dp[i-1][j]*(1-P[i]) + dp[i-1][j-1]*P[i]
        else:
            dp[i][j] = dp[i-1][j]*(1-P[i])
print(sum(dp[N][(N+1)//2:]))
# printdp()
