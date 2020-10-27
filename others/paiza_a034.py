# paiza_a034.py
'''
制約見る前は DP かと思ったけど、制約見たら普通に Bit 全探索でびっくり。
というかPythonでの時間制限がかなりゆるゆる（16秒）なのがびっくり。
このレベルだと Atcoder だったら C 問題で、灰 Diff なんだよなぁ…
'''
import itertools
N, M = map(int, input().split())
status = [(0, 1) for _ in range(N)]
state = list(itertools.product(*status))
prices = []
for i in range(N):
    prices.append(int(input()))
ans = []
for i in state:
    val = i.count(1)
    price = 0
    for j in range(N):
        price += i[j]*prices[j]
    if price <= M:
        ans.append((val, price))
ans = sorted(ans, key=lambda x: (x[0], x[1]), reverse=True)
print(M-ans[0][1])
