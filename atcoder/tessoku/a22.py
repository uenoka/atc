'''
# 問題
ある双六には $N$ 個のマスがあり、スタートから順に $1$ から $N$ までの番号が付けられています。\
この双六では、あなたがマス $i$ $(i = 1, 2, \cdots, N-1)$ にいるとき、以下の 2 種類の行動のうち一方を選ぶことができます。

* マス $A\_i$ に進み、スコア $100$ を得る
* マス $B\_i$ に進み、スコア $150$ を得る

ゴールにたどり着くまでに得られる合計スコアの最大値を出力するプログラムを作成してください。

# 問題概要



# 考察


'''

def fprint(dp):
    for i in dp:
        print(i)

N = int(input())
A = [0] + list(map(int,input().split()))
B = [0] + list(map(int,input().split()))
DP = [0 for _ in range(N+1)]
for i in range(1,N):
    DP[A[i]] = max(DP[A[i]],DP[i]+100)
    DP[B[i]] = max(DP[B[i]],DP[i]+150)
print(DP[N])
