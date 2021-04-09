# validate-binary-search-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Util import createBinaryTree as cbt
from TreeNode import TreeNode
'''
この解法クッソ奇麗だなというのと、引数は初期値指定してあげれば引数の数違っても実行できるからこの書き方ができるというのはなるほどと思った
'''

class Solution:
    def isValidBST(self, root: TreeNode, minVal=float('-inf'), maxVal=float('inf')) -> bool:
        if not root:
            return True
        if root.val <= minVal or root.val>=maxVal:
            return False
        return self.isValidBST(root.left, minVal, min(root.val, maxVal)) and self.isValidBST(root.right, max(minVal,root.val),maxVal)



testcases = [
    # [2, 1, 3],
    # [5, 1, 4, None, None, 3, 6],
    # [1, 1, 1],
    # [5,2,4,2,2,4,4],
    # [5, 4, 6,  None, None, 3, 7],
    # [0, None, 1]
    [120, 70, 140, 50, 100, 130, 160, 20, 55, 75, 110, 119, 135, 150, 200]
]
sol = Solution()
for testcase in testcases:
    root = cbt().create(testcase)
    print(sol.isValidBST(root))
