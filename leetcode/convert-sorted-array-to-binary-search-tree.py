# convert-sorted-array-to-binary-search-tree.py
'''
この解法きれいだなぁ…すごい。
こういう再帰をもっとちゃんと出来るようにしたい。
'''


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        mid = len(nums)//2
        return TreeNode(
            val=nums[mid],
            left=self.sortedArrayToBST(nums[:mid]),
            right=self.sortedArrayToBST(nums[mid+1:]),
        )
