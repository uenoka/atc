# maximum-depth-of-binary-tree.py
'''
言われてみれは普通の深さ優先探索だけど、こういうのをぱっと書くのムズイよなぁ。
とはいえ言われたら出来るようにはなったので、あとは練習次第といった感じかな。
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
