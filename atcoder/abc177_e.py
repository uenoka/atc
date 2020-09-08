# abc177_e.py
'''
基本的な方針（コンテスト中にここまでは気づいた）
配列内に要素すべてに同じ素因数がある → not coprime
配列内の要素すべてに同じ素因数がない → pairwise coprime
配列内の要素いくつかに同じ素因数があるがすべてではない → setwise coprime
そのうえでどうすべきか?
・各要素の素因数分解をする
・それぞれの要素を dict に入れて個数を管理する
・全部が1だったら pairwise, 1つでもNと同じ個数だったら not , そうでなかったら setwise
これであれば、素因数分解部分を除くと O(N) で計算が可能
ただし、素因数分解は O(√N) の計算量がかかるため最大で 10**9 となる TLE してしまう。
そこで osak 法（正式名称?）というアルゴリズムで素因数分解を行う。
'''


def eratosthenes(n):
    D = [0]*(n+1)
    for i in range(2, n+1):
        if D[i] > 0:
            continue
        for j in range(i, n+1, i):
            D[j] = i
    return D


N = int(input())
A = list(map(int, input().split()))
D = eratosthenes(max(A))
dic = {}
for i in A:
    while i != 1:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
        i //= D[i]

isPairwise = True
isNowise = False
for i in dic.items():
    print(i)
    if i[1] > 1:
        isPairwise = False
    if i[1] == N:
        isNowise = True

if isPairwise:
    print("pairwise coprime")
elif isNowise:
    print("not coprime")
else:
    print("setwise coprime")
