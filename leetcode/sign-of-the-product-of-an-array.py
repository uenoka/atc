# sign-of-the-product-of-an-array.py
class Solution:
    def arraySign(self, nums) -> int:
        cnt = 1
        for i in nums:
            if i < 0:
                cnt *= -1
            elif i == 0:
                return 0
        return cnt

testcases = [
    [-1, -2, -3, -4, 3, 2, 1],
    [-1, -2, -3, -4, 3, 2, 1, 0],
    [-1, -2, -3, -4, 3, 2, 1,-1]
]
for nums in testcases:
    sol = Solution().arraySign(nums)
    print(sol)