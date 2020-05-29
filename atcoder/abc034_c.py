# abc034_c.py
'''
逆元の問題
キーワードはフェルマーの小定理、高速な累乗計算、factrial、などなど…
とりあえず理論はあんまりわからないけど、まずはこの手の問題を解説込みで解けたのが良かった。
'''
W,H = map(int,input().split())
mod = 10**9+7
ans = 1
m = W+H-2
for i in range(W+H-2):
    ans *= m
    ans %= mod
    m -= 1
#    print(ans)
import math
w = pow(math.factorial(W-1),mod-2,mod)
h = pow(math.factorial(H-1),mod-2,mod)
#print(w,h)
ans *= (w*h)%mod
print(ans % mod)

