# binary-tree-level-order-traversal.py
'''
この解法すごいな、Queue の長さで for することでうまいこと1つの Queue で制御している。
'''
from TreeNode import TreeNode
from Util import createBinaryTree

class Solution:
    def levelOrder(self, root: TreeNode):
        if root is None:
            return root
        queue = []
        ans = []
        queue.append(root)
        while queue:
            level_node = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_node.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            ans.append(level_node)
        return ans
def createNode(nodeData):
    return createBinaryTree().create(nodeData)

nodeData = [3, 9, 20, None, None, 15, 7]
node = createNode(nodeData)
print(Solution().levelOrder(node))
