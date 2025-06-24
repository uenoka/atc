
'''
# 問題

ALGO 市には $N$ 個の駅と $M$ 個のバス停があり、下図のように道路で結ばれています。 すべての組 $(i,j)$ に対して「駅 $i$ からバス停 $j$ までの所要時間」を足した値はいくつですか？

![Statement](https://img.atcoder.jp/tessoku-book/a37-statement-fix.png)

# 考察

算数チックね。
B * (N*M) + N*sum(Ci) + M*sum(Ai)
こんな感じで出せそう。
これはなんの考察テクニックなんだろう?
'''
N,M,B = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = B*(N*M)
for a in A:
    ans += a*M
for c in C:
    ans += c*N
print(ans)
    