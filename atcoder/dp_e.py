# dp_e.py
'''
D と基本は同じだが制約が
E
  W  = 10**9
  vi = 10**3
D
  W  = 10**5
  vi = 10**9
と変わっている。
さてどうしたものか。
テーブルを D のように持つとメモリ的にも厳しいし計算量的にも O(NW) では間に合わない
DP テーブルを縦=item, 横=価値の総和 で作って、そのテーブルの中に入れるのが重さにする。
その時Wを超えたら更新しないというような形にすることで
この形であれば O( max(vi)*N * N ) で 10^5 くらいで解けるはず
重さの最大値を求めることはできるが、これをどうやって価値にする?
'''


def printdp():
    for i in dp:
        print(i)
        print('-----')


# prepare
N, W = map(int, input().split())
w = [0]
v = [0]
for i in range(N):
    wi, vi = map(int, input().split())
    w.append(wi)
    v.append(vi)
vsum = sum(v)+1
# dp
dp = [[10**9+1 for j in range(vsum)] for i in range(N+1)]
dp[0][0] = 0
for row in range(1, N+1):
    for col in range(vsum):
        if col < v[row]:
            dp[row][col] = dp[row-1][col]
        else:
            current = min(dp[row-1][col], dp[row-1][col-v[row]]+w[row])
            dp[row][col] = current
    # printdp()
ans = 0
for i, v in enumerate(dp[N]):
    if v <= W:
        ans = i
print(ans)
