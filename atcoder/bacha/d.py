'''
# 問題文

空の列 $A$ があります。クエリが $Q$ 個与えられるので、与えられた順番に処理してください。\
クエリは次の $3$ 種類のいずれかです。

* `1 x` : $A$ の最後尾に $x$ を追加する。
* `2` : $A$ の最初の要素を出力する。その後、その要素を削除する。このクエリが与えられるとき、$A$ は空でないことが保証される。
* `3` : $A$ を昇順にソートする。

# 考察
3のときに1回ソートするってことは、それ以降の左は3がもう一度来るまで固定される
クエリ2が来たときに色々と困りそう
セグ木と生配列持っていればいけるかも?
遅延評価のセグ木とかそういうものな気がするな。
クエリ3 が来るまでAにためておいて、3 が来たらセグ木に流し込む
一度セグ木に流し込んだら次のクエリ3が来るまではセグ期の最小値を返す + 最小値を削除するというのをやるのが良い?
→セグ木じゃなくてPriorityQueue で良さそう
'''

import heapq
from collections import deque
Q = int(input())
A = deque()
Ahq = []
heapq.heapify(Ahq)
for _ in range(Q):
    q = input().split()
    if q[0]=='1':
        A.append(int(q[1]))
        # 末尾に追加
    elif q[0]=='2':
        if len(Ahq)==0:
            print(A.popleft())
        else:
            print(heapq.heappop(Ahq))
    else:
        for a in A:
            heapq.heappush(Ahq,a)
        A = deque()