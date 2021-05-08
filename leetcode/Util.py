# Util.py
from TreeNode import TreeNode
from ListNode import ListNode
from collections import deque

class createBinaryTree:
    def create(self,nodeData):
        root = TreeNode(nodeData[0])
        nodeQueue = deque()
        pairQueue = deque()
        nodeQueue.append(root)
        for i in range(1,len(nodeData),2):
            newPair = self.createPair(nodeData,i)
            pairQueue.append(newPair)
            node = nodeQueue.popleft()
            pair = pairQueue.popleft()
            if pair[0] is not None:
                node.left = TreeNode(pair[0])
                nodeQueue.append(node.left)
            if pair[1] is not None:
                node.right = TreeNode(pair[1])
                nodeQueue.append(node.right)

        return root

    def createPair(self,nodeData,i):
        if i+1 >= len(nodeData):
            print('last one!',nodeData[i])
            return [nodeData[i],None]
        return [nodeData[i], nodeData[i+1]]


    def printNode(self, node):
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

class createListNode:
    def create(self,nodeData):
        if not nodeData:
            return None
        node = ListNode(nodeData[0])
        currentNode = node
        for i in nodeData[1:]:
            nextNode = ListNode(i)
            currentNode.next = nextNode
            currentNode = nextNode
        return node


    def printNode(self,node,idx):
        if node is None:
            print("None")
            return
        print(node.val , " -> ",end="")
        return self.printNode(node.next, idx + 1)



# nodeData = [3, 9, 20, None, None, 15, 7]
# node = createBinaryTree().create(nodeData)
# createBinaryTree().printNode(node)
