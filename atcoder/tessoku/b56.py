
'''
# 問題

回文とは、前から読んでも後ろから読んでも変わらない文字列のことを指します。たとえば `abba` や `level` は回文です。

長さ $N$ の文字列 $S$ が与えられます。以下の $Q$ 個のクエリに答えてください。

* $i$ 個目のクエリ：$S\[L\_i, R\_i]$ は回文か？

ただし、$S\[l, r]$ は $S$ の $l$ 文字目から $r$ 文字目までの連続部分文字列のことを指します。

# 考察

回分判定。
文字列を正順と逆順でそれぞれローリングハッシュしておいて、
各クエリの前半と後半のの文字列ハッシュが同じかを見るのが良さそう。

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
rh_asc = RollingHash(S)
s_reversed = ''.join(list(reversed(S)))
rh_desc = RollingHash(s_reversed)

for _ in range(Q):
    l, r = map(int,input().split())
    # 偶奇で分ける
    if (l+r)%2 == 1: # 1文字目も含むので偶数文字
        asc_l = l
        asc_r = (l+r)//2
        # 逆順にした文字列のl、rを見る
        desc_l = len(S) - r + 1
        desc_r = len(S) - asc_r
    else:
        asc_l = l
        asc_r = (l+r)//2 - 1
        desc_l = len(S) - r + 1
        desc_r = len(S) - asc_r - 1
    hash1 = rh_asc.get_hash(asc_l, asc_r)
    hash2 = rh_desc.get_hash(desc_l, desc_r)
    
    # ハッシュ値が同じなら文字列も同じ（高確率）
    if hash1 == hash2:
        print("Yes")
    else:
        print("No")
