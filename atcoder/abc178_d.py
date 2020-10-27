# abc178_d.py
'''
初手では全然わからなかったけど、この解説がすごくわかりやすかった
https://recording-books-japan.blogspot.com/2020/09/atcoderabc178d.html
S を 3 で割ることで最大の求める数列の項数が分かる
1 ～ 最大の項数 の数列で、それぞれ各刻項にまず3をいれて、余った数をどこに入れるかという問題に帰結させる。
例：S=11 の時求める数列のの最大の項数は 11/3 = 3...2 なので 3。
余りは 2 なので3つの項のどこかにこの余った数を割り振ってあげればいい。
そうすると、組み合わせは、ボールの区切りをどこに入れるかと同じ考え方なので重複組み合わせ
||〇〇～〇〇|| の選び方なので、最初の1つ目の区切りは3通り入れる場所がある（|〇|〇| これの各棒線の場所）
2つ目の区切りは4通りある（\|\〇\〇\ これの \ の場所）
ただし \と| は本来区別できないので割る2してあげる必要があるので、この場合3*4/2 = 6 ( 4C2 )になる。
この操作を、1~最大の項数で実施していき、それぞれの答えを足し合わせる（mod の問題なので途中で mod をとる）
'''
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under




S = int(input())
max_terms = S//3
ans = 1
mod=10**9+7
if S<3:
    print(0)
    exit()
if S<7:
    print(1)
    exit()

for i in range(2,max_terms+1):

    remainder = S - 3*i
    ans += cmb(i+remainder-1,remainder)
    ans%=mod
print(ans)

