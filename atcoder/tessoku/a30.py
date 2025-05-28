'''
# 問題

$N! = 1 \times 2 \times \dots \times N$（ $N$ の階乗 といいます）とするとき、以下の式の値を $1000000007$ （素数）で割った余りを出力してください。

$\_n$$\rm{C}$$\_r$ $= \frac{n!}{r! \times (n-r)!}$

なお、答えは「 $n$ 個のモノの中から $r$ 個を選ぶ方法の数」と一致することが知られています。

# 考察
nCr を計算する。

'''
def factorial_mod(n, mod):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % mod
    return fact

def nCr(n, r, mod):
    if r > n:
        return 0
    fact = factorial_mod(n, mod)
    return (fact[n] * pow(fact[r], mod - 2, mod) % mod * pow(fact[n - r], mod - 2, mod) % mod)
def main():
    mod = 1000000007
    n, r = map(int, input().split())
    print(nCr(n, r, mod))
if __name__ == "__main__":
    main()
