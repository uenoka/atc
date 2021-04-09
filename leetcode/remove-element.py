# remove-element.py
'''
これすげーきれいだなぁ
'''
class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j]!= val:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
        print(nums)
        return i

nums =[3,3,3,3,2,2,2,3,2,3,2,2,3,3]
val = 3
sol = Solution().removeElement(nums,val)
print(sol)
