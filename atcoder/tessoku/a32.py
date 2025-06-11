'''
# 問題

$N$ 個の石が積まれた山があり、 $2$ 人のプレイヤーが交互に石を取り合います。\
各プレイヤーは $1$ 回のターンで、以下のいずれかの操作をすることができます。

* 山から $A$ 個の石を取り除く。
* 山から $B$ 個の石を取り除く。

先に石を取り除けなくなった方が負けです。両者が最善を尽くしたとき、先手と後手どちらが勝ちますか。

# 考察


'''
N, A, B = map(int, input().split())
first_win = [False]*(N+1)
for i in range(N+1):
    if i >= A and first_win[i-A] == False:
        first_win[i]=True
    elif i >= B and first_win[i-B] == False:
        first_win[i]=True
    else:
        first_win[i]=False
print('First' if first_win[N] else 'Second')
'''
[0, 0, 0, 1, 1, 1, 0, 0, 1]
First
'''