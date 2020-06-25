# abc149_d.py
def janken(idx,mine):
    if i >= K:
        if flg[i-K] and T[i-K]==T[i]:
            return 0
    flg[i] = True
    if mine=="r":
        return R
    if mine=="p":
        return P
    if mine=="s":
        return S

N, K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()
flg = [False]*N
ans = 0
for i,v in enumerate(T):
    if v=="s":
        ans += janken(i,"r")
    elif v=="r":
        ans += janken(i,"p")
    elif v=="p":
        ans += janken(i,"s")
print(ans)