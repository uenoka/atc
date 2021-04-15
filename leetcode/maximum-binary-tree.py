# maximum-binary-tree.py
'''
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
