# 20200610_yorukatsu_b.py
N = int(input())
A = []
B = []
for i in  range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

push = 0
for i in range(N):
    if (A[N-i-1] + push) % B[N-i-1] != 0:
        push += abs(B[N-i-1] - ((push + A[N-i-1]) % B[N-i-1]))
print(push)
