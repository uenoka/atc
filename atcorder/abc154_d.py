# abc154_d.py
'''
それぞれの期待値を累積和で求めておいて、
累積和[i] - 累積和[i-k] の計算をして最大値を求める。

解法自体は思いついたが、累積和[i] - 累積和[i-k] とするべきところを
sum(累積和[i-k:i]) としていてなかなか合わなかった。
また、それぞれのサイコロの期待値が独立だから和を求めればいい、などの考え方も
正直ちゃんと理解して出来ていたかというと微妙なので、もうちょっと確率とか
勉強したほうがよさそう。
'''
N, K = map(int,input().split())
P = list(map(int,input().split()))

exps = []
_sum = 0
for v in P:
    _sum += (1+v)/2
    exps.append(_sum)

ans = exps[K-1]
for i in range(K,N):
    if ans < exps[i]-exps[i-K]:
        ans = exps[i]-exps[i-K]

print(ans)

