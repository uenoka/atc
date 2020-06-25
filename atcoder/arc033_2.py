# arc033_2.py
'''
要約すると、A,Bの共通文字列の数/A,Bのどちらかに含まれている文字列の数
共通する文字列の数をCとすると求める答えは、かぶったところを引くので
C/(A+B-C) 
になる。
なので単純にCを高速に求めていきたい、という問題になる。
-> Na, Nb が最大 10^5 なので、Hash map 等 O(1) で取得できるデータ構造使えばよい。
Python では set 等を使うとできる。
ただし今回は set で存在する / しないを判定するのが面倒（出来たっけ?エラー返さないっけ?というのがぱっと思い浮かばなかった）だったのと、スニペットにCounterがあったのでこちらで実装。
'''
import collections
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = 0
AC = collections.Counter(A)
BC = collections.Counter(B)
for i, cnt in AC.items():
    C += BC[i]
print(C/(N+M-C))
