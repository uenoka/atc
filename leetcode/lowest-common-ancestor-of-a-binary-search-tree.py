# lowest-common-ancestor-of-a-binary-search-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Util import createBinaryTree
import TreeNode

class Solution:
    def find(self,root,p,q):
        if not root:
            return
        if p.val <= root.val <= q.val:
            return root
        if root.val < p.val:
            print('root', root.val, 'p', p.val, 'q', q.val)
            return self.find(root.right, p, q)
        else:
            print('root', root.val, 'p', p.val, 'q', q.val)
            return self.find(root.left, p, q)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p,q = q,p
        if p.val == q.val:
            return p.val
        return self.find(root,p,q)


testcases = [
    [[6,2,8,0,4,7,9,None,None,3,5], 2, 8],
    [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4],
    [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 5],
    [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 5, 4],
    [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 5, 0],
    [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 5, 5],
]
for t1, t2, t3 in testcases:
    root = createBinaryTree().create(t1)
    p = createBinaryTree().create(t2)
    q = createBinaryTree().create(t3)
    # createBinaryTree().printTree(root)
    # print("===")
    # createBinaryTree().printTree(p)
    # print("===")
    # createBinaryTree().printTree(q)
    # print("===")
    sol = Solution().lowestCommonAncestor(root, p, q)
    print(sol)
