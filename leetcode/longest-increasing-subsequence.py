# longest-increasing-subsequence.py
'''
DP でやる感じだとは思うがどうやるかね…
'''
class Solution:
    def lengthOfLIS(self, nums) -> int:
        memo = [0]*len(nums)
        def dp(idx,tmp_nums):
            if idx>=len(nums):
                return 1
            print(idx,memo)
            if len(tmp_nums) <= 1:
                memo[-1] = 1
                return 1
            if memo[idx]!=0:
                return memo[idx]
            for i in range(idx,len(tmp_nums)):
                print(i)
                if tmp_nums[idx] < tmp_nums[i]:
                    memo[idx] = dp(idx+i, tmp_nums) + 1
                    break
            return memo[idx]
        dp(0,nums)
        print(memo)
        return max(memo)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
sol = Solution().lengthOfLIS(nums)
print(sol)
