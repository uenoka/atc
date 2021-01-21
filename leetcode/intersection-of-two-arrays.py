# intersection-of-two-arrays.py
class Solution:
    def intersection(self, nums1, nums2):
        num1 = set(nums1)
        num2 = set(nums2)
        ans = []
        for i in num1:
            if i in num2:
                ans.append(i)
        return ans


sol = Solution()
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
sol.intersection(nums1, nums2)
