# find-numbers-with-even-number-of-digits.py
class Solution:
    def findNumbers(self, nums) -> int:
        ans = 0
        for i in nums:
            s = str(i)
            if len(s) % 2 == 0:
                ans += 1
        return ans


sol = Solution()
nums = [12, 345, 2, 6, 7896]
print(sol.findNumbers(nums))
