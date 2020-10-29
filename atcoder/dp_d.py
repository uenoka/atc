# dp_d.py
'''
ちょっとだけDPわかってきた気がする
これはpypyじゃないとTLEしてしまうので、こういうのをテストケースで補完できるようにしたいなぁ
'''


def printdp():
    for i in dp:
        print(i)
    print('-----')


N, W = map(int, input().split())
V = [[0, 0]]
for i in range(N):
    A = list(map(int, input().split()))
    V.append(A)
dp = [[0 for j in range(W+1)] for i in range(N+1)]
for item in range(1, N+1):
    for weight in range(1, W+1):
        if weight < V[item][0]:
            dp[item][weight] = dp[item-1][weight]
        else:
            dp[item][weight] = max(
                dp[item-1][weight], dp[item-1][weight-V[item][0]]+V[item][1])
        # printdp()
print(dp[N][W])
