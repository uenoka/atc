# maximum-subarray.py
'''
株価のやつもそうだけど、この手の問題解くのすごく苦手だなぁ…
'''


class Solution:
    def maxSubArray(self, nums) -> int:
        newNum = nums[0]
        maxTotal = nums[0]
        for i in range(1, len(nums)):
            print('newNum, maxTotal', newNum, maxTotal)
            newNum = max(nums[i], nums[i] + newNum)
            maxTotal = max(newNum, maxTotal)
        print('newNum, maxTotal', newNum, maxTotal)
        return maxTotal


sol = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sol.maxSubArray(nums))
