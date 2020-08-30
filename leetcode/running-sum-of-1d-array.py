# running-sum-of-1d-array.py
'''
いわゆる累積和。
英語で runnning sum というらしい。
今まで Cumulative sum だと思ってた。
'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        _sum = 0
        for i in nums:
            _sum += i
            ans.append(_sum)
        return ans


sol = Solution()
nums = [1, 2, 3, 4]
print(sol.runningSum(nums))
