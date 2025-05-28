'''
# 問題

$a^b$ を $1000000007$ $(=10^9+7)$ で割った余りを計算してください。

# 考察
繰り返し二乗法のやつ
再帰で書けるとかっこいいけどうまく書けないんだよなぁ

'''
def calc(a,b):
    mod = 1000000007
    if b == 0:
        return 1
    if b == 1:
        return a % mod
    half = calc(a, b // 2)
    if b % 2 == 0:
        return (half * half) % mod
    else:
        return (half * half * a) % mod

a,b = map(int,input().split())
print(calc(a,b))