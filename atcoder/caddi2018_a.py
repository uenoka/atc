# caddi2018_a.py
'''
基本的には P を素因数分解して、N個以上ある素因数をかけ合わせたものが答え
ただ2N 個以上ある場合に注意（素因数の個数を N で割った商を答えに入れていくとよさそう）
計算量的には素因数分解は O(√N) なので、それぞれの素因数の数がどのくらいになるかによる。
'''


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


N, P = map(int, input().split())
primes = factorization(P)
ans = 1
for v, cnt in primes:
    if cnt/N >= 1:
        ans *= (v**(cnt//N))
print(ans)
