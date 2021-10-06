# binary-tree-paths.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Util import createBinaryTree
import TreeNode
from typing import List
import copy
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        def dfs(root,path):
            if not root:
                return
            path.append(root.val)
            if root.left:
                leftPath = copy.deepcopy(path)
                dfs(root.left, leftPath)
            if root.right:
                rightPath = copy.deepcopy(path)
                dfs(root.right, rightPath)
            if not root.left and not root.right:
                paths.append(path)
        dfs(root,[])
        return ['->'.join(list(map(str,path))) for path in paths]

testcases = [
    [1, 2, 3, None, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1],
    []
]

for testcase in testcases:
    root = createBinaryTree().create(testcase)
    sol = Solution().binaryTreePaths(root)
    print(sol)
