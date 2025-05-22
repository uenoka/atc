'''
# 問題
$N$ 個のブロックが並べられており、左から順に $1, 2, \cdots, N$ と番号が付けられています。\
あなたは、以下の 2 種類の操作を何回か行うことで、すべてのブロックを取り除きたいです。

* 今ある中で **一番左** のブロックを取り除く。
* 今ある中で **一番右** のブロックを取り除く。

ブロック $i$ $(i = 1, 2, \cdots, N)$ をブロック $P\_i$ より先に取り除いた場合、$A\_i$ 点が得られます。\
合計得点としてあり得る最大値を出力するプログラムを作成してください。

# 問題概要

N 個のブロックがあり、それぞれに、 Pi より先に取ったら Ai 点もらえるという情報が書いてある。
左右どちらかから一つずつ取る操作を繰り返したときに、どのような取り方が特典を最大化出来るか。

# 考察

単純に考えて愚直にやっていこうとすると最大化できない。
例えば入力サンプル1の
```
4
4 20
3 30
2 40
1 10
```
だと、愚直にやっていく(つまり左右のどちらが特典が高いかを見ていく)と50点が最大。(1,2 を最初に取る)
しかし、よく見てみると1,4,3,2の順で取ると60点を取れる。
DP[l][r] で考える。l は左のindex, r は右の index
DP[l][r] が両端のとき、明らかに得点は 0(DP[0][N] = 0)
DP[l][r] が両端ではないとき、必ず DP[l-1][r] または DP[l][r+1] からボールを取った
あとに到達するので、それをもとに計算をしていく。
'''

def fprint(dp):
    for i in dp:
        print(i)

N = int(input())
P = [0]
A = [0]
def score1(l,r):
    return A[l] if P[l]<=r and l<=P[l] else 0

def score2(l,r):
    return A[r] if P[r]<=r and l<=P[r] else 0

for n in range(N):
    p, a = map(int,input().split())
    P.append(p)
    A.append(a)
DP = [[0 for _ in range(N+1)] for _ in range(N+1)]
for l in range(1,N+1):
    for r in range(N,l-1,-1):
        if r == N and l == 1:
            DP[l][r] = 0
        elif r == N:
            DP[l][r] = DP[l-1][r] + score1(l-1,r)
        elif l == 1:
            DP[l][r] = DP[l][r+1] + score2(l,r+1)
        else:
            DP[l][r] = max(
                            DP[l-1][r] + score1(l-1,r),
                            DP[l][r+1] + score2(l,r+1)
                        )
m = 0
for i in range(N+1):
    m = max(DP[i][i],m)

print(m)