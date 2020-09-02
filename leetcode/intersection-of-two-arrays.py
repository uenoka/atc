intersection-of-two-arrays.py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = set(num1)
        num2 = set(num2)
        ans = []
        for i in num1:
            if i in num2:
                ans.append(i)
        return ans

sol = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
sol.intersection(num1,num2)
