# n-ary-tree-postorder-traversal.py
'''
Recursive solution is trivial, could you do it iteratively?
とのことなので再帰と for, while 両方で解けるとよい。
postorder traversal とか preorder traversal は N 分木の走査方法で重要らしいのでこれを機に学習するとよさそう。
解けるだけでなくてきちんとデータ構造とアルゴリズムの知識として知っておく。
'''


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node):
        pass
