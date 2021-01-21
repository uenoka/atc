# abc167_c_recursion.py
'''
bit 全探索だから再帰でやろうとしたけど無理だった、、、再帰でやろうとするとムズイ。。。
とりあえず復習で出来たというところだけでもよし
'''

import itertools
N, M, X = map(int, input().split())
skills = [0]*M
C = []
A = []

min_price = 10**9
for i in range(N):
    c, *a = map(int, input().split())
    C.append(c)
    A.append(a)
flg = True
status = [(0, 1) for _ in range(N)]
state = list(itertools.product(*status))
for pattern in state:
    price = 0
    gakuryoku = [0]*M
    for i, v in enumerate(pattern):
        if v == 1:
            price += C[i]
            for j in range(M):
                gakuryoku[j] += A[i][j-1]
        if price <= min_price and min(gakuryoku) >= X:
            min_price = price
            flg = False
if flg:
    print(-1)
else:
    print(min_price)
