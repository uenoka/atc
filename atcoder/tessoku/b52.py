'''
# 問題

$N$ 個のボールが一列に並べられています。これらのボールの最初の色は文字列 $A$ で与えられます。

ボール $i$ の色は $A$ の $i$ 文字目で表されており、黒の時 $A\_i$ は `#`、白の時 $A\_i$ は `.`　となっています。

以下のシミュレーションを行うとき、最終的なボールの色はどうなりますか。

* まず、キューに整数 $X$ を追加し、ボール $X$ を青で塗る。

* その後、キューが空になるまで以下の操作を繰り返す。

  * キューの先頭要素 ($\text{pos}$) を削除する
  * ボール $\text{pos}-1$ が白のとき、これを青で塗り、キューに $\text{pos}-1$ を追加する
  * ボール $\text{pos}+1$ が白のとき、これを青で塗り、キューに $\text{pos}+1$ を追加する

# 考察

'''
from collections import deque
N, X = map(int,input().split())
A = list(input())
queue = deque([X])
A[X-1] = '@'
while queue:
    pos = queue.popleft()
    if pos-2 >= 0 and A[pos-2] == '.':
        A[pos-2] = '@'
        queue.append(pos-1)
    if pos < len(A) and A[pos] == '.' :
        A[pos] = '@'
        queue.append(pos+1)
print(*A,sep='')