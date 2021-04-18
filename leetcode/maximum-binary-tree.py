# maximum-binary-tree.py
'''
概要：整数値の入った配列が与えられる。以下の操作で得られる二分木を構築せよ。
・配列の最大値をrootとする
・rootの左側にある配列を用いて再帰的に左側の木構造を構築する
・同様に、rootの右側にある配列を用いて再帰的に右側の木構造を構築する
実装は指定された処理をそのまま実装。
配列のまま触ると結構遅そう（368 ms）
多分だけどcollectionsとかで適切に最大値とインデックス取れればい感じかな？
-> O(N) のスタックでの解法があるっぽい。これはちょっと面白そう
'''
from TreeNode import TreeNode
from Util import createBinaryTree


class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        if not nums:
            return None
        m = max(nums)
        maxidx = nums.index(m)
        node = TreeNode(m)
        print('now is ', nums)
        print('max idx is ', maxidx)
        if maxidx != 0:
            print('m', m, 'left', nums[:maxidx-1])
            node.left = self.constructMaximumBinaryTree(nums[:maxidx])
        if maxidx < len(nums)-1:
            print('m', m, 'right', nums[maxidx+1:])
            node.right = self.constructMaximumBinaryTree(nums[maxidx+1:])
        return node
