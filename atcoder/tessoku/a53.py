
'''
# 問題

以下の $3$ 種類のクエリを高速に処理する、販売システムを実装してください。

* クエリ $1$：価格が $x$ 円の商品が追加される。
* クエリ $2$：今ある商品の中の最小価格を答える。
* クエリ $3$：最も安い商品が $1$ つ売れる。

ただし、最初は商品が $1$ つもなく、与えられるクエリの数は $Q$ 個であるとします。

# 考察

優先度付きキューやるだけ。
もし生で実装するならどうするかな?
やっぱり linked list 作って insert 時ににぶたんでソートを保つ感じかな?

'''
import heapq
Q = int(input())
pq = []
heapq.heapify(pq)
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        heapq.heappush(pq,int(q[1]))
    elif q[0] == '2':
        print(pq[0])
    elif q[0] == '3':
        heapq.heappop(pq)