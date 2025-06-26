'''
# 問題

長さ $N$ の文字列 $S$ が与えられます。以下の $Q$ 個のクエリを処理してください。

* $i$ 個目のクエリ：$S\[a\_i, b\_i]$ と $S\[c\_i, d\_i]$ は一致するか？

ただし、$S\[l, r]$ は $S$ の $l$ 文字目から $r$ 文字目までの連続部分文字列のことを指します。

# 考察

これわかんないな。クエリのたびにキャッシュしておいても結局全部違う位置の比較でやられたら O(NQ) で間に合わない。
でも前処理しておいてもO(N^2)になるから同じく間に合わない。
それともハッシュ関数で短くすればよいのか?これよくわからんな。
ハッシュが正解だけど、そもそもハッシュの計算量がわからん、あと mod もどうすべきかわからん、衝突もあるしわからんってなってる。
これがいわゆるローリングハッシュなのか。

'''

class RollingHash:
    def __init__(self, s, base=257, mod=10**9+7):
        self.base = base
        self.mod = mod
        n = len(s)
        
        # 累積ハッシュ値とべき乗を前計算
        self.hash = [0] * (n + 1)
        self.pow = [1] * (n + 1)
        
        for i in range(n):
            self.hash[i + 1] = (self.hash[i] * self.base + ord(s[i])) % self.mod
            self.pow[i + 1] = (self.pow[i] * self.base) % self.mod
    
    def get_hash(self, l, r):
        """S[l-1:r]のハッシュ値を取得（1-indexedから0-indexedに変換）"""
        l -= 1  # 1-indexedを0-indexedに
        r -= 1
        return (self.hash[r + 1] - self.hash[l] * self.pow[r - l + 1]) % self.mod

N, Q = map(int,input().split())
S = input()

# ローリングハッシュのインスタンスを作成
rh = RollingHash(S)

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    
    # 2つの部分文字列のハッシュ値を計算
    hash1 = rh.get_hash(a, b)
    hash2 = rh.get_hash(c, d)
    
    # ハッシュ値が同じなら文字列も同じ（高確率）
    if hash1 == hash2:
        print("Yes")
    else:
        print("No")