# arc106_b.py
'''
連結成分内で和が同じであればOKって感じかな。
'''
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
glaph = [[] for i in range(N+1)]
for i in range(M):
    c, d = map(int, input().split())
    glaph[c].append(d)
seen = [False]*N
