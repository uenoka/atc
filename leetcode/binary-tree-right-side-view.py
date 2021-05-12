# binary-tree-right-side-view.py
'''
BFSで各レイヤの一番右側を保持する感じで実装する
うまく実装できなかったなぁ…Queueを2つ使って各レベルをトラバースするの一回見たけど全然できるようにならない…そしてどこにあったか忘れた…
参考実装はDFSだけどレベルを引数に渡すことでうまいこと右側を保持している
'''

from Util import createBinaryTree
import TreeNode
import queue
from typing import List
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def traverse(node,level):
            if not node:
                return
            if self.max_level < level:
                self.res.append(node.val)
                self.max_level = level
            traverse(node.right,level+1)
            traverse(node.left,level+1)
        self.res = []
        self.max_level = 0
        traverse(root,1)
        return self.res
testcases = [
    [],
    [1,None,3],
    [1,2,3,None,5,None,4]
]
for nodes in testcases:
    root = createBinaryTree().create(nodes)
    sol = Solution().rightSideView(root)
    print(sol)
