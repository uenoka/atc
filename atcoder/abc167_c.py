# abc167_c.py
N, M, X = map(int,input().split())
C = []
A = []
for i in range(N):
    c,*a = map(int,input().split())
    C.append(c)
    A.append(a)

def calc_price(C,s):
    ans = 0
    for i,v in enumerate(s):
        if v==1:
            ans+=C[i]
    return ans


import itertools
status = [(0, 1) for _ in range(N)]
state = list(itertools.product(*status))
#print(state)
ans = 10**9+7
flg = -1
for s in state:
    price = 0
    gakuryoku = [0]*M
    for j,v in enumerate(s):
        if v == 1:
            price+=C[j]
            for k in range(M):
                gakuryoku[k] += A[j][k]
        if min(gakuryoku)>=X and ans > price:
            ans = price
            flg=0
if flg==-1:
    print(-1)
else:
    print(ans)

