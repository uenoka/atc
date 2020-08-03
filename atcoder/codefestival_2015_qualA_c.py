# codefestival_2015_qualA_c.py
'''
部分点解法はAを降順ソートして大きいのから順に消す。
宿題をやる場合 → TからAiを引く
宿題を写す場合 → TにAi-Biを足してあげる（すでにAを引いているので、差分を足すことで表現できる）
と言えるので、次のような処理の流れにする
Ai-Biの値をCiとして配列で保存しておく
TからAの和を引く（→すべての宿題を自分で解く）
そもそもTが正なら写す必要はなく答えは0
Tが負なら、Ai-Biの値が大きい順に足していく（＝たくさん時間が節約できる宿題を写す）
Tが正になったら何個写したか出力
Tが負のままならすべての宿題を写しても間に合わないので-1を出力
想定解法では逆にすべての宿題を写すからスタートしているが、やっていることは同じ
'''
N, T = map(int,input().split())
A = 0
B = 0
C = []
for i in range(N):
    a,b = map(int,input().split())
    c = a - b
    A += a
    B += b
    C.append(c)
C.sort(reverse=True)
cnt = 0
T -= A
for i in C:
    if T>=0:
        break
    T += i
    cnt += 1
if T<0:
    print(-1)
else:
    print(cnt)
    
