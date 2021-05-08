# diameter-of-binary-tree.py
'''
隣接リストとかであれば親とこの行き来ができるので、各NodeでDSFして最大を求めることができるが、TreeNodeだとできない。
なのである1つのNodeの左右に最大何Nodeぶら下がっているかをカウントしてあげて、その和が最大のものを見つける。
解法まではわかるものの実装できず。
こういう再帰とかグラフ系はまだまだ難しいなぁ
'''
from Util import createBinaryTree
from TreeNode import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.longestPath = 0
        def calcLongestPath(root):
            if not root:
                return 0
            left_path = calcLongestPath(root.left)
            right_path = calcLongestPath(root.right)
            self.longestPath = max(self.longestPath,left_path + right_path)
            return max(left_path,right_path) + 1
        calcLongestPath(root)
        return self.longestPath

testcases = [
    # [1,2],
    [1,2,3,4,5]
]

for nodes in testcases:
    root = createBinaryTree().create(nodes)
    sol = Solution().diameterOfBinaryTree(root)
    print(sol)