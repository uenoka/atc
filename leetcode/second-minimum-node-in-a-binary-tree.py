# second-minimum-node-in-a-binary-tree.py
'''
解けたと思ったけど結構難しい、出来ない…
結構深いネストの中に2番目に小さい値がいることもあるから、うまいこと再帰的に取って来ないとダメそう?
→いや、これむしろ深さ優先で解いちゃだめだ、全部の要素見ながらじゃなきゃだから、幅優先探索的に解かなきゃいけない。
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        result = set()
        import collections
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            result.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result = sorted(list(result))
        if len(result) < 2:
            return -1
        return result[1]
