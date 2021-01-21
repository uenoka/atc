# set-mismatch.py
'''
これは競プロにありそうな問題。
配列の和とsetの和とかをいじくるのはよくある。
'''


class Solution:
    def findErrorNums(self, nums):
        numsSet = set(nums)
        duplicated = sum(nums) - sum(numsSet)
        missed = len(nums)*(len(nums)+1)//2 - sum(numsSet)
        return [duplicated, missed]


sol = Solution()
nums = [1, 4, 3, 4, 5, 6]
print(sol.findErrorNums(nums))
