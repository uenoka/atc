# minimum-operations-to-make-the-array-increasing.py
class Solution:
    def minOperations(self, nums) -> int:
        ans = 0
        length = len(nums)
        for i in range(length-1):
            ans += 0 if nums[i] < nums[i+1] else nums[i]+1 - nums[i+1]
            nums[i+1] = nums[i+1] if nums[i] < nums[i+1] else nums[i] + 1
        return ans
testcases = [
    [1, 1, 1],
    [1, 5, 2, 4, 1],
    [8]
]
for nums in testcases:
    sol = Solution().minOperations(nums)
    print(sol)
