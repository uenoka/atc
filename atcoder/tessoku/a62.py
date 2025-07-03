
'''
# 問題

各頂点に $1,2,\dots,N$ の番号がついた、 $N$ 頂点 $M$ 辺の無向グラフが与えられます。\
$i$ 番目の辺は頂点 $A\_i$ と頂点 $B\_i$ とを結んでいます。\
このグラフ全体が連結であるかどうか判定して以下のように出力してください。

* もしグラフ全体が連結であれば、 `The graph is connected.` と出力する
* そうでなければ、 `The graph is not connected.` と出力する

# 考察

DFS の問題。
でも連結の判定だから UnionFind やりたくなるね。
多分DFSでやるなら1つめの Node で DFS して seen を管理して、全部の Node が Seen になったらOK、みたいな感じかな。

'''
from atcoder.dsu import DSU
N, M = map(int,input().split())
uf = DSU(N)
for _ in range(M):
    a,b = map(int,input().split())
    uf.merge(a-1,b-1)
print('The graph is connected.') if uf.size(0)==N else print('The graph is not connected.')