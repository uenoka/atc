
'''
# 問題

頂点数 $N$、辺数 $M$ のグラフが与えられます。頂点には $1$ から $N$ までの番号が付けられており、$i$ 番目の辺は頂点 $A\_i$ と $B\_i$ を双方向に結んでいます。 それぞれの $k$ について、「頂点 $k$ と隣接している頂点の番号」をすべて出力するプログラムを作成してください。

# 考察

グラフ！！！
隣接グラフを全部出す基本問題的な感じ。
これであれば特にグラフであることを気にせず、配列のidx をnode ,中身を

'''

N, M = map(int,input().split())
glaph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    glaph[a].append(b)
    glaph[b].append(a)
for i in range(1, N+1):
    print(f"{i}: {{{', '.join(map(str, sorted(glaph[i])))}}}")
