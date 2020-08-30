# create-target-array-in-the-given-order.py


class Solution:
    def createTargetArray(self, nums, index):
        length = len(nums)
        ans = list()
        for i in range(length):
            ans.insert(index[i], nums[i])
        return ans


sol = Solution()
nums = [1, 2, 3, 4, 0]
index = [0, 1, 2, 3, 0]
print(sol.createTargetArray(nums, index))
