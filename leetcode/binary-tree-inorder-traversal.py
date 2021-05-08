# binary-tree-inorder-traversal.py
'''
この程度のものならある程度こんなだろうなぁでいけるようになってきた！
基礎知識感があるからMedeumなのはちょっと過大評価感があるけど、基礎知識になるものをサクッとできるのうれしい。
'''
from typing import List
from Util import createBinaryTree
import TreeNode
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def traverse(root,traversal):
            if not root:
                return []
            traverse(root.left,traversal)
            traversal.append(root.val)
            traverse(root.right, traversal)
            return traversal
        return traverse(root,[])

def printTree(root, parent = None, lr = 'parent'):
    if not root:
        return
    print('parent is', parent, 'val is ', root.val, 'place', lr)
    printTree(root.left, root.val,'left')
    printTree(root.right, root.val,'right')
testcases = [
    [1,2,3,4,5,6,7,8,9],
    [1,2,4,5,6,7,8,9],
    [1,2,None,4,5,6,7,8,9],
    [1],
    [],
]
for nodes in testcases:
    root = createBinaryTree().create(nodes)
    sol = Solution().inorderTraversal(root)
    print(sol)
