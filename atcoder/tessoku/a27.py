'''
# 問題

$A$ と $B$ の最大公約数を求めてください。

# 考察
最大公約数
python には math.gcd があるけど一応アルゴリズムを書いていこう。
ユークリッドの互除法で出来る。
'''
def gcd(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a%b
        elif b > a:
            b = b%a
        else:
            break
    return max(a,b)
    
A,B = map(int,input().split())

print(gcd(A,B))