# maximum-product-of-two-elements-in-an-array.py

class Solution:
    def maxProduct(self, nums) -> int:
        nums.sort()
        return (nums[-2]-1)*(nums[-1]-1)


sol = Solution()
nums = [1, 5, 4, 5]
print(sol.maxProduct(nums))
