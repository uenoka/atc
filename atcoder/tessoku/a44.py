
'''
# 問題

長さ $N$ の配列 $A = \[A\_1, \ldots, A\_N]$ があり、最初はすべての $i$ について $A\_i = i$ となっています。あなたは配列に対して $Q$ 回の操作を行います。$j$ 回目の操作は文字列 $Query\_j$ で表されます。

* 変更操作：$Query\_j = \ $ `1 x y` のとき、$A\_x$ の値を $y$ に変更する
* 反転操作：$Query\_j = \ $ `2` のとき、配列 $A$ を逆順にする
* 取得操作：$Query\_j = \ $ `3 x` のとき、$A\_x$ の値を答える

すべての取得操作に対して、正しく答えるプログラムを作成してください。

# 考察

愚直にやろうとするとO(Q*NlogN)かかる(Q回のクエリ全てにおいてソートされた場合)
さてどうするか。
ソートしなくてもインデックス持っておけば行けそうにも見えるが、結構処理が複雑か?

'''

N, Q = map(int,input().split())
A = [i+1 for i in range(N)]
order = 0 # 0 = asc, 1 = desc
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        if order == 0:
            A[q[1]-1] = q[2]    
        else:
            A[N - q[1]] = q[2]
    elif q[0] == 2:
        order = 1 - order
    if q[0] == 3:
        if order == 0:
            print(A[q[1]-1])
        else:
            print(A[N - q[1]])