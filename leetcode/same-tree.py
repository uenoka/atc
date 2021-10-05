# same-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import TreeNode
from Util import createBinaryTree

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def isSameNode(pNode,qNode):
            if not pNode and not qNode:
                return True
            if not pNode or not qNode:
                return False
            if pNode.val != qNode.val:
                return False
            return isSameNode(pNode.left, qNode.left) and isSameNode(pNode.right, qNode.right)
        return isSameNode(p,q)




testcases = [
    [[1, 2, 1], [1, 1, 2]],
    [[1, 2, 3], [1, 2, 3]],
    [[1, 2],[1, None, 2]],
    [[1], [1]],
    [[], []],
]
for p,q in testcases:
    p = createBinaryTree().create(p)
    q = createBinaryTree().create(q)
    createBinaryTree().printTree(p)
    createBinaryTree().printTree(q)

    sol = Solution().isSameTree(p,q)
    print(sol)
