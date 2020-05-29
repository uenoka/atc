# ALDS1_3_B.py
n = int(input())

A = [int(input()) for _ in range(n)]

_min = A[0]
_max = -(10**9)
for i in range(1, n):
    _max = max(_max, A[i] - _min)
    _min = min(_min, A[i])
print(_max)
