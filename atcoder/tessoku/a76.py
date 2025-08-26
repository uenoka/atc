
'''
# 問題

川幅が $W$ メートルである KYOPRO 川には、 $N$ 個の足場が一直線上に並べられており、西から順に $1$ から $N$ までの番号が付けられています。足場 $i$ $(1 \leq i \leq N)$ は西岸から $X\_i$ メートルの位置にあります。

太郎君は東方向のジャンプを繰り返すことで、西岸から東岸まで移動しようと思いました。しかし、一回のジャンプで飛ぶ距離は長すぎても短すぎてもダメであり、 $L$ メートル以上 $R$ メートル以下でなければなりません。移動方法は全部で何通りありますか。

# 考察

基本のDP。Flog 2 とほぼ同じかな?
→ TLE する

これむず、これ星5はあるだろ…全然解けない。全部知ってるアルゴリズムだけど累積和の取り方とか全然理解できない。
あー、なるほど、本の書き方が悪すぎる。dpで出した値を累積和で保存して再利用するということか。

'''
from bisect import bisect_left, bisect_right

N, W, L, R = map(int,input().split())
X = [0]+list(map(int,input().split()))+[W]
mod = 1000000007
dp = [0 for _ in range(N+2)]
dp[0] = 1
sum = [0 for _ in range(N+3)]  # サイズを1つ大きく
sum[0] = 0  # 番兵
sum[1] = 1  # sum[1] = dp[0] = 1

for i in range(1,N+2):
    min_prev_pos = X[i]-R
    max_prev_pos = X[i]-L
    posL = bisect_left(X, min_prev_pos)
    posR = bisect_right(X, max_prev_pos) -1
    posL = max(0, posL)
    posR = min(i-1, posR)
    
    if posL<= posR:
        # sum[j+1] = dp[0] + ... + dp[j] の定義
        # dp[posL] + ... + dp[posR] = sum[posR+1] - sum[posL]
        dp[i] = (sum[posR+1] - sum[posL]) % mod
    
    sum[i+1] = (sum[i] + dp[i]) % mod

print(dp[N+1] % mod)