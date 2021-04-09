# Remove-Duplicates-from-Sorted-Array.py
class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1
nums = [0,1,1,2,3,4,4,4,5]
sol = Solution().removeDuplicates(nums)
print(sol)