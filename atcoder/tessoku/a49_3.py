
'''
# 問題

長さ $20$ の配列 $X = \[X\_1, X\_2, \cdots, X\_{20}]$ があります。最初は、すべての要素がゼロとなっています。\
あなたは配列に対して $T$ 回の操作を行います。$i$ 手目では、以下のいずれかを選択します。

> **操作A：**$X\_{P\_i}, X\_{Q\_i}, X\_{R\_i}$ に $+1$ を加算する。\
> **操作B：**$X\_{P\_i}, X\_{Q\_i}, X\_{R\_i}$ に $-1$ を加算する。

各操作が終わった後、「$X\_j=0$ となる $j$ の個数」だけスコアが加算されます。 すなわち、スコアの加算は全部で $T$ 回行われます。\
できるだけスコアが大きくなるような操作手順を求めてください。

# 考察

毎回入力を受け取ったら足したら何点、引いたら何点、を計算して高い方を選択する。
37454
'''

T = int(input())
X = [0 for _ in range(20)]
for t in range(T):
    p,q,r = map(int,input().split())
    xpi = X[p-1]
    xqi = X[q-1]
    xri = X[r-1]
    add_zero_count = 0
    sub_zero_count = 0
    if xpi-1==0:
        sub_zero_count+=1
    if xqi-1==0:
        sub_zero_count+=1
    if xri-1==0:
        sub_zero_count+=1
    if xpi+1==0:
        add_zero_count+=1
    if xqi+1==0:
        add_zero_count+=1
    if xri+1==0:
        add_zero_count+=1
    if add_zero_count > sub_zero_count:
        print('A')
        X[p-1] += 1
        X[q-1] += 1
        X[r-1] += 1
    else:
        print('B')
        X[p-1] -= 1
        X[q-1] -= 1
        X[r-1] -= 1