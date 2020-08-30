# range-sum-of-bst.py
'''
簡単とはいえ再帰でこういうの書けたのうれしい。
'''


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        if L < root.val < R:
            return root.val + rangeSumBST(root.left, L, R)+rangeSumBST(root.right, L, R)
        return rangeSumBST(root.left, L, R)+rangeSumBST(root.right, L, R)
