# abc079_b.py
# 基本はフィボナッチ数列のメモ化再帰と同じ形で解く。
# いい勉強になるので何度も解きたい問題

def calc_luca(n):
    if n==0:
        return luca[0]
    if n==1:
        return luca[1]
    if luca[n]!=0:
        return luca[n]
    luca[n] = calc_luca(n-1) + calc_luca(n-2)
    return luca[n]
N = int(input())
luca = [0]*(N+1)
luca[0] = 2
luca[1] = 1
print(calc_luca(N))
#print(luca)