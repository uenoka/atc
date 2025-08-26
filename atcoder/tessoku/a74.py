
'''
# 問題

$1$ から $N$ までの整数が一個ずつ書かれた $N \times N$ のマス目 $P$ が与えられます。太郎君は、

* 隣接する 2 つの行を交換する
* 隣接する 2 つの列を交換する

という 2 種類の操作を繰り返すことで、すべての $k$ に対して「整数 $k$ が上から $k$ 行目・左から $k$ 列目のマスに存在する」ようにしたいです。最小何回の操作が必要ですか。

# 考察

こんなのが与えられる
0 1 0 0
0 0 2 0
0 0 0 3
4 0 0 0
このとき、こうしたい
1 0 0 0
0 2 0 0
0 0 3 0
0 0 0 4
この最小手数を求める。
Nは100以下なので最大100*100の行列が渡される

直感的に考えると、愚直に縦でバブルソート、横でバブルソートみたいな感じだけど合ってるかな?
そう考えると2次元で見ないで良くて、縦と横で配列用意してあげてそれぞれをソートして回数を保持するのが良さそう。
0 1 0 0
0 0 2 0
0 0 0 3
4 0 0 0
この例のときには
縦 = [1,2,3,4]
横 = [4,1,2,3]
なので、縦入れ替え0回、横入れ替え3回で行ける
入力サンプルだと
0 0 2 0
3 0 0 0
0 0 0 4
0 1 0 0
縦 = [3,1,2,4]
横 = [2,3,4,1]
で縦の入れ替え2回、横の入れ替え3回の合計5回
'''
def bubble_sort_and_count(data):
    n = len(data)
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swaps += 1
    return swaps

N = int(input())
P = [list(map(int,input().split())) for _ in range(N)]
H = []
for h in range(N):
    for w in range(N):
        if P[h][w] != 0:
            H.append(P[h][w])
W = []
for w in range(N):
    for h in range(N):
        if P[h][w] != 0:
            W.append(P[h][w])
print(bubble_sort_and_count(H)+bubble_sort_and_count(W))
