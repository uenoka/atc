# search-in-a-binary-search-tree.py
'''
何とかAC、ただこれがきれいなのかどうかが分からないな
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        print(root.val)
        if root.val == val:
            return root
        if root.left:
            node = self.searchBST(root.left, val)
            if node:
                return node
        if root.right:
            node = self.searchBST(root.right, val)
            if node:
                return node
