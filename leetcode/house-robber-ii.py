# house-robber-ii.py
'''
動的計画法かなー？
写経してみた。
先頭と末尾を外してそれぞれ最大になるようにDPしていく感じ。
そもそも先頭と末尾を外して出来るかってのが良くわからないなぁ…
'''

class Solution:
    def rob(self, nums) -> int:
        def houseRobber(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],nums[i] + dp[i-2])
            return dp[-1]
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))



test_cases = [
    [0],
    [2, 3, 2],
    [2, 1, 3, 1, 4, 1, 1, 100, 1, 1],
    [1, 2, 3, 1]
]

for nums in test_cases:
    sol = Solution().rob(nums)
    print(sol)
