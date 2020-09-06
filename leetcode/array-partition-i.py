# array-partition-i.py

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i, v in enumerate(nums):
            if i % 2 == 0:
                ans += v
        return ans


sol = Solution()
arr = [1, 4, 3, 2]
print(sol.arrayPairSum(arr))
