# symmetric-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1回目は鏡を間違えて、各Nodeの左右が同じという判定でWA
2回目はrootの左右でQueueを持っておいてそれぞれに、左から、右から要素を追加してBFSしてQueueの先頭の値を比較したけどNoneを飛ばしてQueueに入れると微妙にずれるのでWA
最後にどうにかこうにかそれっぽいものを条件式に付け加えることでAC
勘違いしたりうまく実装できなかったり、要素が1つの時や鏡ではないそれっぽいものをはじくみたいなのができなかったり、うまく実装はできなかったけど答え見ずに実装できたのはよかった。
Mediumくらいあってもいい気がするけど、とはいえ簡単なBFS、Queueの扱いかたみたいなのでできるからEasyなのかなぁ…

'''
import TreeNode
from Util import createBinaryTree
import queue
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if (root.left and not root.right) or (not root.left and root.right):
            return False
        if not root.left.val == root.right.val:
            return False
        leftQueue = queue.Queue()
        rightQueue = queue.Queue()
        leftQueue.put(root.left)
        rightQueue.put(root.right)
        while not leftQueue.empty() or not rightQueue.empty():
            leftnode = leftQueue.get()
            rightnode = rightQueue.get()
            if not leftnode.val == rightnode.val:
                return False

            if leftnode.left and rightnode.right:
                leftQueue.put(leftnode.left)
                rightQueue.put(rightnode.right)
            else:
                return False
            if leftnode.right and rightnode.left:
                leftQueue.put(leftnode.right)
                rightQueue.put(rightnode.left)
            else:
                return False
        return True

testcases = [
     [1,2,2,3,4,4,3],
     [1,2,2,None,3,None,3]
]
for node in testcases:
    root = createBinaryTree().create(node)
    sol = Solution().isSymmetric(root)
    print(sol)