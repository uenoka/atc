# binary-tree-zigzag-level-order-traversal.py
'''
基本的には、全部を左から見ていく-> 段数が奇数だったら逆にするこのときすべてQueueに入れておくことで簡略化できる。
全部を左から見ていきましょうみたいな問題に if を追加するだけでよい。
-> https://leetcode.com/problems/binary-tree-level-order-traversal
これができればできるねという感じ。
'''
from TreeNode import TreeNode
from Util import createBinaryTree

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        import collections
        queue = collections.deque()
        ans = []
        queue.append(root)
        order = 0
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if order % 2 == 1:
                level.reverse()
            ans.append(level)
            order += 1
        return ans


root = [3, 9, 20, None, None, 15, 7]
bt = createBinaryTree().create(root)
sol = Solution().zigzagLevelOrder(bt)
print(sol)
