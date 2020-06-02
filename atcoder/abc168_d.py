# abc168_d.py
'''
1から各頂点へ幅優先探索して最短経路を探す
見つけるときに目印を持っておいて、N-1の配列に前の場所を記載する
'''
N, M = map(int, input().split())
route = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    route[A].append(B)
    route[B].append(A)
