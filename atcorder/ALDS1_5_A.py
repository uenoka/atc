# ALDS1_5_A.py
memo = []


def rec(m, a, idx, id):
    if a == m:
        return True
    if idx >= len(A):
        return False
    _next = A[idx]
    return rec(m, a+_next, idx+1, id+"1") or rec(m, a, idx+1, id+"0")


N = int(input())
A = list(map(int, input().split()))
input()
M = list(map(int, input().split()))

for i in M:
    if rec(i, 0, 0, "0"):
        print('yes')
    else:
        print('no')
