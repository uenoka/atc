# find-all-numbers-disappeared-in-an-array.py
class Solution:
    def findDisappearedNumbers(self, nums):
        length = len(nums)+1
        hashMap = {}
        for i in nums:
            if i in hashMap:
                hashMap[i] +=1
            else:
                hashMap[i] = 1
        ret = []
        for i in range(1,length):
            if i not in hashMap:
                ret.append(i)
        return ret


testcases = [
    [4, 3, 2, 7, 8, 2, 3, 1],
    [1, 1]
]

for nums in testcases:
    sol = Solution().findDisappearedNumbers(nums)
    print(sol)
