
'''
# 問題

頂点数 $N$、辺数 $M$ のグラフが与えられます。頂点には $1$ から $N$ までの番号が付けられており、辺 $i$ は頂点 $A\_i$ と $B\_i$ を双方向に結ぶ長さ $C\_i$ の辺です。このグラフの**最小全域木**における辺の長さの総和を求めてください。

# 考察

問題文から最小全域木。
ただ、最小全域木とはなんぞやというところ。
最小全域木 : ある連結されたグラフの辺をいくつか選び、木構造にした際に、辺の重さが最小のもの。
求め方 : 辺をソートして、短い方から以下の手順で追加していくことで求めることができる。
1. 辺が結んでいるノードは連結成分かを判定する
2. 連結でなければ連結する
3. 連結であれば飛ばす
4. これをすべての辺で見ていく
連結かどうかの判定にUnionFindを使用する。
これをクラスカル法というらしい。
'''
from atcoder.dsu import DSU
N, M = map(int,input().split())
A = []
B = []
C = []
for i in range(M):
    a,b,c = map(int,input().split())
    A.append(a-1)
    B.append(b-1)
    C.append((c,i))
C = sorted(C, key=lambda x: x[0])
ans = 0
uf = DSU(N)
for c,i in C:
    if not uf.same(A[i],B[i]):
        ans += c
        uf.merge(A[i],B[i])
print(ans)