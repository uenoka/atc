# third-maximum-number.py
class Solution:
    def thirdMax(self, nums) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) < 3:
            return nums[0]
        return nums[2]

testcases = [
    [1, 2],
    [3, 2, 1],
    [2, 2, 3, 1]
]

for nums in testcases:
    sol = Solution().thirdMax(nums)
    print(sol)

