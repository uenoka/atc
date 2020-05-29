# abc095_b.py
N, M = map(int,input().split())
K = [int(input()) for i in range(N)]
K.sort()
ans = len(K)
M-=sum(K)
ans += (M//min(K))
print(ans) 