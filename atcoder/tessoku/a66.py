
'''
# 問題

頂点数 $N$ のグラフに対して、以下の $2$ 種類のクエリを高速に処理してください。

* **クエリ $1$**：頂点 $u$ と頂点 $v$ を双方向に結ぶ辺を追加する。
* **クエリ $2$**：頂点 $u$ と頂点 $v$ は同じ連結成分に属するかを答える。

ただし、最初はグラフに辺が一本もなく、与えられるクエリの数は $Q$ 個であるとします。

# 考察

UnionFind。

'''
from atcoder.dsu import DSU
N, Q = map(int,input().split())
uf = DSU(N)
for _ in range(Q):
    q,u,v = map(int,input().split())
    if q == 1:
        uf.merge(u-1,v-1)
    else:
        print('Yes' if uf.same(u-1,v-1) else 'No')