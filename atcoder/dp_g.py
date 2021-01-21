# dp_g.py
'''
longest path
概要：有向グラフがあるので、その中で一番長いPathを見つけて、長さを出力する、という問題。

考えたこと：多分だけど各 node を表す配列を持っておいて、それぞれの node について何回隣の node に移れるかというのを幅優先探索見ていって、
到達したところの node の配列に到達した今までの最大経路数を記載していく、その配列で一番大きい値を書いていく、みたいな感じ?
どっちかというとメモ化再帰のグラフ版（各 node の最大経路を保存しておいて、再検索をしなくてよいというイメージ）
なんとなくだけど最短経路の逆版っぽそうだから、ダイクストラ法がDP見たいというのはこういうところからきているのかも。
イメージとしては、自分の隣の node の持っている最大経路をもらうような感じ?
ただ、順番がちゃんとしていないと容易にバグりそう、これをどうやってやるか。
到達した node が 0 だったら再帰的に検索（本当に0の場合は検索が発生しないはずだからOK）、
数字があったらその値をもらって帰る
でもこれだとなんか O(NM) になりそう…?
'''
import sys
sys.setrecursionlimit(500000)


def dfs(n):
    if dp[n] != -1:
        return dp[n]
    if not nodes[n]:
        dp[n] = 0
        return 0

    max_path = 0
    for i in nodes[n]:
        current = dfs(i)
        if max_path < current:
            max_path = current
    dp[n] = max_path + 1
    return dp[n]


N, M = map(int, input().split())
nodes = [[] for i in range(N+1)]
for i in range(M):
    bef, aft = map(int, input().split())
    nodes[bef].append(aft)

dp = [-1]*(N+1)

for i in range(1, N+1):
    dfs(i)

print(max(dp))
# print(nodes)
# print(dp)
