# joi2010ho_a.py
'''
地味に問題文に10^5で割ったあまりとあって無事WA。
それ以外は添え字が結構わからなくなったりしたりするけど
だいたいの累積和の感覚はつかめてきた。
突然コンテストで出てきたときに今度は解けるようにしたい。
'''
N, M = map(int,input().split())
mod = 10**5
dist_sum = [0]
pre = 0

for _ in range(N-1):
    dist = int(input())
    pre += dist
    dist_sum.append(pre)
# print(dist_sum)
_from = 0
move = 0
for _ in range(M):
    to = int(input())
    move += abs(dist_sum[_from+to]-dist_sum[_from])
#    print("form, to :",_from,to,",dist from to:", dist_sum[_from], dist_sum[_from + to],",move :",move)
    _from = _from + to
print(move%mod)
