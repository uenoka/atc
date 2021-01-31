# Util.py
from TreeNode import TreeNode
from collections import deque

class createBinaryTree:
    def create(self,nodeData):
        root = TreeNode(nodeData[0])
        nodeStack = []
        pairQueue = deque()
        nodeStack.append(root)
        for i in range(1,len(nodeData),2):
            newPair = [nodeData[i], nodeData[i+1]]
            pairQueue.append(newPair)
            node = nodeStack.pop()
            pair = pairQueue.popleft()
            if pair[1] is not None:
                node.right = TreeNode(pair[1])
                nodeStack.append(node.right)
            if pair[0] is not None:
                node.left = TreeNode(pair[0])
                nodeStack.append(node.left)
        return root


    def printNode(self,node):
        if node is None:
            return
        left = node.left
        right = node.right
        if left is not None and right is not None:
            print(node.val, left.val, right.val)
        elif left is None and right is not None:
            print(node.val, left.val, right.val)
        elif right is None and left is not None:
            print(node.val, left.val, right.val)
        else:
            print(node.val, 'null', 'null')
        if left is not None:
            self.printNode(left)
        if right is not None:
            self.printNode(right)




# nodeData = [3, 9, 20, None, None, 15, 7]
# node = createBinaryTree().create(nodeData)
# createBinaryTree().printNode(node)
