# construct-binary-tree-from-preorder-and-inorder-traversal.py
'''
preorder, inorder, postorder, level-order についての知識と取り扱い方を問う問題。
LeetCode だと https://leetcode.com/explore/learn/card/data-structure-tree/ で学べる。
・preorder の先頭はTreeのrootになる
・inorder のroot を挟んで左側はrootの左側の部分木、右側はrootの右側の部分木
・部分木でも同様の構造をしている
という再帰的な形をとるので、それをうまく扱えられれば回答できる。
この構造にはたどり着いたが実装が厳しい…
'''
from Util import createBinaryTree as cbt
from TreeNode import TreeNode

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def array_to_tree(left,right):
            nonlocal preorder_index
            if left > right:return None
            root_value = preorder[preorder_index]
            root= TreeNode(root_value)
            preorder_index += 1
            root.left = array_to_tree(left, inorder_index_map[root_value]-1)
            root.right = array_to_tree( inorder_index_map[root_value]+1,right)
            return root
        preorder_index = 0
        inorder_index_map= {}
        for index,value in enumerate(inorder):
            inorder_index_map[value] = index
        return array_to_tree(0,len(preorder)-1)
 
testcases = [
    [[1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7]],
    [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]],
]
for preorder, inorder in testcases:
    sol = Solution().buildTree(preorder,inorder)
    print(sol)
