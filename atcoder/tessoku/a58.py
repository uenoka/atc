
'''
# 問題

長さ $N$ の数列 $A = (A\_1, A\_2, \ldots, A\_N)$ があり、最初はすべての要素が $0$ になっています。以下の $2$ 種類のクエリを処理してください。

* **クエリ 1**：$A\_{\mathrm{pos}}$ の値を $x$ に更新する。
* **クエリ 2**：$A\_l, A\_{l+1}, \ldots, A\_{r-1}$ の最大値を答える。

ただし、与えられるクエリの数は全部で $Q$ 個であるとします。

# 考察

まぁ区間の最大値だから何かしら二分木のデータ構造持ってやるんだろうなとは思う。多分。

'''

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)  # 4倍のサイズで安全に確保
    
    def update(self, node, start, end, idx, val):
        """idx位置の値をvalに更新"""
        if start == end:
            # 葉ノード
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2*node, start, mid, idx, val)
            else:
                self.update(2*node+1, mid+1, end, idx, val)
            # 子ノードの最大値で更新
            self.tree[node] = max(self.tree[2*node], self.tree[2*node+1])
    
    def query(self, node, start, end, l, r):
        """区間[l, r]の最大値を取得"""
        if r < start or end < l:
            # 範囲外
            return 0
        if l <= start and end <= r:
            # 完全に含まれる
            return self.tree[node]
        # 部分的に含まれる
        mid = (start + end) // 2
        left_max = self.query(2*node, start, mid, l, r)
        right_max = self.query(2*node+1, mid+1, end, l, r)
        return max(left_max, right_max)
    
    def update_point(self, idx, val):
        """外部インターface: idx位置をvalに更新"""
        self.update(1, 0, self.n-1, idx, val)
    
    def range_max(self, l, r):
        """外部インターface: 区間[l, r]の最大値"""
        return self.query(1, 0, self.n-1, l, r)

N, Q = map(int, input().split())
seg_tree = SegmentTree(N)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # クエリ1: 更新
        pos, x = query[1], query[2]
        seg_tree.upddate_point(pos - 1, x)  # 0-indexedに変換
    else:
        # クエリ2: 区間最大値
        l, r = query[1], query[2]
        print(seg_tree.range_max(l - 1, r - 2))  # 0-indexedに変換