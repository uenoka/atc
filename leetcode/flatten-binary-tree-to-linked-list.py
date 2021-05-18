# flatten-binary-tree-to-linked-list.py
'''
stack に深さ優先探索で積んでいって、そのあとにrootの左に入れていく感じがよさそう？
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        self.stack = []
        def dfs(node):
            if not node:
                return node
            if not node.left and not node.right:
                return node
            self.stack.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        for i in range(len(self.stack)-1):
            self.stack[i].right = self.stack[i+1]
            self.stack[i].left = None
