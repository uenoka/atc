# house-robber.py
'''
DP の基本問題。
ただこれが難しい…
考え方を知るみたいな記事を読み込んでいくのがいいのかなぁ。
'''
class Solution:
    def rob(self, nums) -> int:
        dp = [0] * len(nums)
        if not nums:
            return 0
        idx = 2
        if len(nums)<3:
            return max(nums)
        dp[0]=nums[0]
        dp[1]=nums[1]

        while idx < len(nums):
            if idx==2:
                dp[idx] = nums[idx] + nums[idx-2]
            else:
                dp[idx]= nums[idx]+max(dp[idx-2],dp[idx-3])
            idx += 1
            print(dp)
        return max(dp[-1],dp[-2])

sol = Solution()
nums = [1,2,3,1]
print(sol.rob(nums))
