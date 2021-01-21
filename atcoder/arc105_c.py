# arc105_c.py
'''
必須：ラクダの体重の最大値≦橋の最小の耐荷重
並び順決める→小さい順 or 大きい順にソートされていない状態が最適な場合はある？

'''
N, M = map(int,input().split())
W = list(map(int,input().split()))
L = []
V = []
for _ in range(M):
    l,v = map(int,input().split())
    L.append(l)
    V.append(v)
if min(V)>max(W):
    print(-1)
    exit()
