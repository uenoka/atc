
'''
# 問題

$N$ 頂点 $M$ 辺の無向グラフが与えられます。各頂点には $1$ から $N$ までの番号が付けられており、$i$ 番目の辺は頂点 $A\_i$ と頂点 $B\_i$ を結んでいます。

$1$ 以上 $N$ 以下の全ての整数 $k$ について、以下の問いに答えてください。

> 頂点 $1$ から頂点 $k$ まで、辺を何本かたどって移動することを考えるとき、たどるべき辺の本数の最小値を出力せよ。ただし、移動不可能な場合は $-1$ を出力せよ。

# 考察

最短経路問題。普通に幅優先探索でもいい気がするね。
頂点1から頂点kへ行くための最短経路を求める。

'''
from collections import deque

def fprint(L):
    for l in L:
        print(l)

N, M = map(int,input().split())
glaph = [[] for _ in range(N+1)]
seen = [-1 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int,input().split())
    glaph[A].append(B)
    glaph[B].append(A)
queue = deque()
queue.append(1)
seen[1] = 0
while queue:
    n = queue.popleft()
    for i in glaph[n]:
        if seen[i] == -1:
            seen[i] = seen[n]+1
            queue.append(i)
for i in seen[1:]:
    print(i)
