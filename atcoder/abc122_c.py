# abc122_c.py
'''
累積和でACがある箇所を管理する方針で行く。
右隣がCとなっているAを管理する累積和を持って置く。
添え字のところがめっちゃ面倒でどうするのか要復習
'''
N, Q = map(int, input().split())
S = input()
_sum = 0
cumsum = [0]*(N+1)

for i in range(N):
    if not i == N-1:
        if S[i] == "A" and S[i+1] == "C":
            _sum += 1
    cumsum[i+1] = _sum

for q in range(Q):
    l, r = map(int, input().split())
    print(cumsum[r-1]-cumsum[l-1])
