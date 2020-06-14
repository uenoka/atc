# 20200612_yorukatsu_c.py
N, K = map(int,input().split())
M = [int(input()) for i in range(N)]
M.sort()
lis = [0]*(N-K+1)
for i in range(N-K+1):
    lis[i] = abs(M[i]-M[i+K-1])
print(min(lis))
