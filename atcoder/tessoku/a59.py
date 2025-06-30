'''
# 問題

長さ $N$ の数列 $A = (A\_1, A\_2, \ldots, A\_N)$ があり、最初はすべての要素が $0$ になっています。以下の $2$ 種類のクエリを処理してください。

* **クエリ 1**：$A\_{\mathrm{pos}}$ の値を $x$ に更新する。
* **クエリ 2**：$A\_l, A\_{l+1}, \ldots, A\_{r-1}$ の合計値を答える。

ただし、与えられるクエリの数は全部で $Q$ 個であるとします。

# 考察

セグ木セグ木。

'''
class SegmentTree:
    def __init__(self, n, operation="sum", identity=0):
        """
        n: 配列サイズ
        operation: "sum" or "max" or "min"
        identity: 単位元（sum:0, max:-inf, min:inf）
        """
        self.n = n
        self.operation = operation
        self.identity = identity
        self.tree = [identity] * (4 * n)
        
        # 演算関数を設定
        if operation == "sum":
            self.op = lambda x, y: x + y
        elif operation == "max":
            self.op = lambda x, y: max(x, y)
        elif operation == "min":
            self.op = lambda x, y: min(x, y)
    
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
            # 子ノードを演算で結合
            self.tree[node] = self.op(self.tree[2*node], self.tree[2*node+1])
    
    def query(self, node, start, end, l, r):
        """区間[l, r]のクエリ結果を取得"""
        if r < start or end < l:
            # 範囲外
            return self.identity
        if l <= start and end <= r:
            # 完全に含まれる
            return self.tree[node]
        # 部分的に含まれる
        mid = (start + end) // 2
        left_result = self.query(2*node, start, mid, l, r)
        right_result = self.query(2*node+1, mid+1, end, l, r)
        return self.op(left_result, right_result)
    
    def update_point(self, idx, val):
        """外部インターface: idx位置をvalに更新"""
        self.update(1, 0, self.n-1, idx, val)
    
    def range_query(self, l, r):
        """外部インターface: 区間[l, r]のクエリ"""
        return self.query(1, 0, self.n-1, l, r)

N, Q = map(int, input().split())
seg_tree = SegmentTree(N, operation="sum", identity=0)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # クエリ 1: 更新
        pos, x = query[1] - 1, query[2]  # 0-indexedに変換
        seg_tree.update_point(pos, x)
    elif query[0] == 2:
        l, r = query[1], query[2]
        # [l, r) を 0-indexedの [l-1, r-2] に変換
        # r-1 が最後の要素なので、0-indexedでは r-2
        left_idx = l - 1
        right_idx = r - 2  # r-1 を 0-indexedに変換
        print(seg_tree.range_query(left_idx, right_idx))