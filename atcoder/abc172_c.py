# abc172_c.py
N, M ,K= map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0
cnt = []
a_sum = 0
b_sum = 0
for i in range(N):
    a_sum += A[i]
    while a_sum + b_sum <= K:
        