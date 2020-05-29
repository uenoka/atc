# GRL_1_A.py
'''
単一始点最短経路の問題。
グラフの扱い方
-> array で idx : [(ni,di),(nj,dj),...] というような形で、頂点->(頂点,重み),(頂点,重み) と扱う。
Queue の扱い方
通常の Queue だと O(V^2) となるので、優先度付きキューを使う。
（二分ヒープによる優先度付きキューだと O((V+E)logV)、フィボナッチヒープだと O(V+ElogV)）
priority queue は (重み,頂点) で書く（heapq が前者を優先度として扱うため）
heapify はしなくても,普通の2次元リストで heappop 党派利用で切るっぽい。謎。
'''
def printh(qu):
    while qu:
        print("q",h.heappop(qu))

import heapq as h
# 最初の入力
V, E, r = map(int,input().split())
# グラフの初期化
adj = [[] for i in range(V)]

# グラフの構築
for e in range(E):
    s, t, d = map(int,input().split())
    adj[s].append((t,d))

for i,v in enumerate(adj):
    print(i,v)
# 各頂点の、スタートからの距離（最初は巨大な値で初期化）
INF = 10**18
dist = [INF for _ in range(V)]
# スタート地点は 0
dist[r] = 0

q = [(0,r)]
while len(q)!=0:
    di,v = h.heappop(q)
    if di > dist[v]:continue
    for next_v, cost in adj[v]:
        if di+cost < dist[next_v]:
            dist[next_v] = di + cost
            h.heappush(q, (dist[next_v],next_v))

for d in dist:
    if d == INF:
        print("INF")
    else:
        print(d)
