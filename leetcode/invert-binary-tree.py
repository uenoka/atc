# invert-binary-tree.py
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        current = root
        current.left, current.right = root.right, root.left
        self.invertTree(current.left)
        self.invertTree(current.right)
        return current
