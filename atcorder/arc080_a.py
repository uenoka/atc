# arc080_a.py
'''
数列内の 4 の倍数の個数を X
数列内の奇数の個数を Y とすると X >= Y となればよい
-> 違った
4の倍数と2の倍数が混在している場合、2の隣には奇数はどのみち来れないため
一か所にまとめておくことで一つの奇数と同等なものとして扱える。
なので4の倍数でなく2の倍数の数がある場合には奇数の数を一つ増やして
同じ判定をしてあげればいい
'''
N = int(input())
A = list(map(int,input().split()))
X = 0
Y = 0
Z = 0
for i in A:
    if i % 4 == 0:
        X += 1
    elif i % 2 == 1:
        Y += 1
    elif i % 2 == 0:
        Z = 1
Y+=Z
# print(X,Y,Z)
if X+1 >= Y:
    print('Yes')
else:
    print('No')