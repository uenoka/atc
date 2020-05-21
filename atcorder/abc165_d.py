# abc165_d.py
'''
コンテスト中に解けなかったので解説AC
値の増減はBの周期（Bまで行くとまた0に戻ってその範囲内では単調増加）
f(x) = floor(A*x/B) - A * floor(x/B) とすると答えは
f( min(B-1,N) ) になるので O(1) で解ける。
この問題、B の周期で 0 ~ A-1 の値を行き来することまではわかっていたが
for の最大を無駄に A, B, N の比較で作ろうとしてバグらせて終わった。
'''

import math
def f(x):
    return math.floor(A*x/B)

A, B, N = map(int, input().split())
print(f(min(B-1,N)))
