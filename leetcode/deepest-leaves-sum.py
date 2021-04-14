#deepest-leaves-sum.py
'''
最初DFSでどうにかこうにかしようとしてダメで、誤読に気づく（Leafならすべて足してよいものと思っていた）
BFSで実装しようにもどう最後のレベルかみればよいのかわからず迷って結局解説AC
普通に幅優先探索していって、そのレベルでの和を取ってあげるというすごくシンプルでいい解法だった。（あと、今入っているNodeの数がレベルのノードの数というのもなるほどとなったのでこれはとても良い練習になりそう）
'''
from Util import createBinaryTree
from TreeNode import TreeNode
from collections import deque


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = deque()
        q.append(root)
        while q:
            sums = 0
            levelNodes = len(q)
            for _ in range(levelNodes):
                node = q.popleft()
                sums += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return sums

testcases = [
    [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8],
    [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
]
for nodes in testcases:
    root = createBinaryTree().create(nodes)
    sol = Solution().deepestLeavesSum(root)
    print(sol)
