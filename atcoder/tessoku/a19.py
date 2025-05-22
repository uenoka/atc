'''

# 問題概要

ナップザック問題

# 考察
基本っちゃ基本だけどむずいよなぁ。
a19 と同じようなイメージで、重さを横軸、縦をアイテム、で各値がそのアイテムを使用するときの価値の最大値
で最後のアイテムまで見切ったあとに最大値を求める
'''

def fprint(dp):
    for i in dp:
        print(i)

N, W = map(int,input().split())

DP = [[0 for _ in range(W+1)] for _ in range(N+1)]
VW = [[0,0]]
for n in range(N):
    w,v = map(int,input().split())
    VW.append([w,v])

for n in range(1,N+1):
    for w in range(1,W+1):
        if w < VW[n][0]:
            DP[n][w] = DP[n-1][w]
        else:
            DP[n][w] = max(DP[n-1][w],DP[n-1][w-VW[n][0]] + VW[n][1])
print(max(DP[N]))