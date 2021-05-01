# maximum-level-sum-of-a-binary-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
どうにか2つQueue使ってトラバースするような感じでやっていったけど結局うまくいかず。
DFS でレベルを保持して行く回答が奇麗でよかったのでこっちでAC
うまく実装できなかった方針もうちょっとちゃんとできるようにしておきたいところ
'''

from TreeNode import TreeNode
from Util import createBinaryTree
from collections import defaultdict


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levels ={}

        def sum_vals(root, depth):
            if root:
                if depth not in levels.keys():
                    levels[depth] = root.val
                else:
                    levels[depth] += root.val
                sum_vals(root.left,  depth+1)
                sum_vals(root.right, depth+1)

        sum_vals(root, 1)
        return max(levels, key=levels.get)



testcases = [
    [1, 7, 0, 7, -8, None, None],
    [989, None, 10250, 98693, -89388, None, None, None, -32127]
]
for nodes in testcases:
    root = createBinaryTree().create(nodes)
    sol = Solution().maxLevelSum(root)
    print(sol)
