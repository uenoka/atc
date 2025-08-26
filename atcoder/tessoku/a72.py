'''
# 問題

縦 $H$ 行、横 $W$ 列のマス目があります。上から $i$ 行目・左から $j$ 列目のマス $(i, j)$ の色は $c\_{i,j}$ であり、$c\_{i,j}$ = `.` のとき白色、 $c\_{i,j}$ = `#` のとき黒色で塗られています。

あなたは「ある行またはある列を選び、すべて黒で塗り替える」という操作を $K$ 回まで行うことができます。最大で何個のマスを黒くすることができますか。

# 考察

2次元累積和っぽそうな見た目。どう解くか。
黒を1,白を0として管理してみるとどうだろう?
それとも制約がそんなないなら全探索してみるのもありか?
全探索解がWA。
愚直に選んでしまうと同じ数のときにどっち選ぶとかがありそうには思うがどうみるか。
縦横どこを選ぶかのDPみたいなことができる??
あーちがう愚直解は全探索になってなかった。
解説読む。
全探索するなら最大110個のH,Wから10選ぶから 110C10 = 110~100まで10回かけて10-1で割るから直感的に
10**2**10 位あるので無理とわかる。
で、Hの値が小さいことに着目すると、Hの選び方はたかだか最大 2**10 = 1024
このそれぞれのパターンのときに、Wのどれを選ぶと良いかを全探索して、最大値を特定する。
考え方としては、全探索の工夫をして計算量削減、Bit全探索、さらにソートでWを効率良く求めるという3つの考え方と手法を
抑えておくというめっちゃ良問。
そして実装がかなり大変。
これ、Hの制約を見てHでまずBit全探索しているけど、W<HのときK!=H になってめっちゃめんどいから、縦横を入れ替えてもっと汎用的にやれるといいなという気持ち
この条件のときにHでまずBit全探索するとKの数超えちゃって変になりそう
'''
def prints(l):
    for i in l:
        print(i)

H, W, K = map(int,input().split())
glid = []
for i in range(H):
    glid.append(list(input()))
# print('start')
# prints(glid)
import copy
import itertools
status = [(0, 1) for _ in range(H)]
states = list(itertools.product(*status))
ans = 0
for state in states:
    # まずは横を選ぶ(H), K から実行した回数を引く
    tmp_glid = copy.deepcopy(glid)
    remain_step = K
    for h in range(H):
        if remain_step == 0:
            break
        if state[h] == 1:
            remain_step -= 1
            tmp_glid[h] = ['#' for _ in range(W)]
    # 次に縦を選ぶ(W)
    column = []
    for w in range(W):
        cnt = 0
        for h in range(H):
            if tmp_glid[h][w]=='.':
                cnt += 1
        column.append([cnt,w])
    column.sort(reverse=True)
    if remain_step>0:
        for k in range(remain_step):
            for h in range(H):
                tmp_glid[h][column[k][1]] = "#"
    # print(state)
    # prints(tmp_glid)
    tmp_ans = 0
    for h in range(H):
        for w in range(W):
            if tmp_glid[h][w] == '#':
                tmp_ans += 1
    ans = max(ans,tmp_ans)
print(ans)