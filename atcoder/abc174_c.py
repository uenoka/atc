# abc174_c.py
'''
考え方
7,77,777,... というのは
A1 = 7
An = 10*A(n-1) + 7
の数列と考えられる。
また、下記の mod の性質から、次項は mod をとってから計算することができる。
An mod K = (10*A(n-1) + 7) mod K
⇔ (10*A(n-1) mod K + 7 mod K ) mod K


前提となる知識
mod の性質
・(a+b)mod k と a mod k + b mod k は等しい
・(a*b)mod k と (a mod k * b mod k) mod k は等しい
'''
K = int(input())
s = 7
flg = False
cnt = 0

for i in range(K+1):
    cnt += 1
    if s % K == 0:
        flg = True
        break
    s *= 10
    s %= K
    s += 7

if flg:
    print(cnt)
else:
    print(-1)
