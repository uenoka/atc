# arc054_b.py
'''
現時点でP年かかる計算がムーアの法則でx年後に 2^x/1.5 倍に短縮される。
最短でどれくらいの時間で終わるか。
0 < P <= 10^18
Pは小数点下4桁までの実数
例：
P = 3.000
ans - 2.8708930019

P = 1000000000000000000.0000
ans = 90.1855078128
年に一回だけ計算を走らせることができるとかなら普通の探索でいいが、どうもそうじゃなさそう。
評価関数は f = x + P/2^(x/(3/2)) になるので、グラフ描画をしてみると（下のサイト参照）凸関数であることがわかる。
Pの値をいじってみると、P > 0 において下に凸であることがわかる（すべての値でいじれはしないが、Pが大きくなっても下に凸なことが変わらない。）
なので、微分してあげると最小値がわかるっぽい。
微分の勉強をせねばならぬ。
あと、整数値以外の二分探索も勉強したほうがいい。
あと、三分探索（高々1つの極限しかない関数の極限を求めるアルゴリズムも利用できる。）
http://www.allisone.co.jp/html/Notes/Mathematics/Function/Convex_Concave_function.html
'''
import time
import math
# f(x)を微分した関数。この関数自体は自分で手で計算して出さないといけない。大変。
def fd(x):
    return 1 + P*math.log(2**(-1/1.5)) * (2**(-x/1.5))

def f(x):
    return x + P/2**(x/1.5)

P = float(input())
# 二分探索で解を求める
left = 0
right = P
start = time.time()
# print("start",start)
while True:
    mid = (left+right)/2
    fdmid = fd(mid)
    if fdmid==0:
        break
    elif fdmid<0:
        left = mid
    else:
        right = mid
    now = time.time()
    # print("now",now)
    if now - start > 1:
        break


print(f(mid))
