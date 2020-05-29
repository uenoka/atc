# ALDS1_5_A.py


def rec(a, use):
    if use >= N:
        memo[a] = True
        return
    _next = A[use]
    rec(a+_next,use+1)
    rec(a,use+1)


N = int(input())
A = list(map(int, input().split()))
Q = int(input())
M = list(map(int, input().split()))

memo = [False]*2000
rec(0, 0)
# print(memo)
for i in M:
    if memo[i]:
        print('yes')
    else:
        print('no')
