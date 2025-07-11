
'''
# 問題

重み付き無向グラフに対する最短経路問題を解いてください。 具体的には、以下のようなグラフが与えられるとき、頂点 $1$ から各頂点までの最短経路長を求めてください。

* 頂点数は $N$ 、辺数は $M$ である
* $i$ 番目の辺は頂点 $A\_i$ と頂点 $B\_i$ を結び、長さは $C\_i$ である

なお、以降の説明では、頂点 $1$ から頂点 $k$ までの最短経路長を $\operatorname{dist}\[k]$ とします。

# 考察

正の重み付き無向グラフに対する最短経路問題。ダイクストラだね。
どうやるんだっけねぇ。

'''
import heapq

def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [float('inf')] * n # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost

n,m = map(int,input().split())
e = [[] for _ in range(n)]
for _ in range(m):
    a,b,t = map(int,input().split())
    a,b = a-1, b-1
    e[a].append((t, b))
    e[b].append((t, a))

dist = dijkstra(0)
for d in dist:
    if d == float('inf'):
        print(-1)
    else:
        print(d)