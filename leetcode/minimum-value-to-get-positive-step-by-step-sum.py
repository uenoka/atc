# minimum-value-to-get-positive-step-by-step-sum.py


class Solution:
    def minStartValue(self, nums) -> int:
        cumsum = [0]*len(nums)
        tmp = 0
        for i, v in enumerate(nums):
            tmp += v
            cumsum[i] = tmp
        return max(-1 * min(cumsum) + 1, 1)


sol = Solution()
nums = [1, 2]
# nums = [-3, 2, -3, 4, 2]
print(sol.minStartValue(nums))
