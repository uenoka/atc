# kth-smallest-element-in-a-bst.py
'''
BST の特性とかを知ってればもしかしたら結構いい計算量まで落とせるかもだが、
いったんは全部探索→探索済みを保持して最後にソート→k番目の大きさの値を返す方法で実装
計算量は O(NlogN) （探索のO(N), ソートにO(NlogN), もしかしたらsetとかで効率化できる？）
→ set は list に直すときにおそらくソート済みにしてくれるようなのでソート分不要になるっぽいから早くなるかも（56ms -> 52ms）
Inorder traversal だと2分探索木では小さい順になるから、O(N)で探索できるっぽい、なるほど。
Follow up も面白いと思うからきちんと読んでおくとよさそう。
'''
from Util import createBinaryTree
import TreeNode
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def travarse(root):
            if not root:
                return
            self.seen.add(root.val)
            travarse(root.left)
            travarse(root.right)
        self.seen = set()
        travarse(root)
        self.seen = list(self.seen)
        return self.seen[k-1]


testcases = [
    [[5,3,6,2,4,None,None,1],3],
    [[3,1,4,None,2], 1]
]
for nodes,k in testcases:
    root = createBinaryTree().create(nodes)
    sol = Solution().kthSmallest(root, k)
    print(sol)