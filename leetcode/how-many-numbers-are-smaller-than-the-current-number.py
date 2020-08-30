# how-many-numbers-are-smaller-than-the-current-number.py
'''
O(N^2)の愚直解法
多分ソートしてやるともうちょっと早くなりそう
'''


class Solution:
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    cnt += 1
            ans.append(cnt)
        return ans


'''
ソートしてあげる解法
ソートする→Hashmapにidxと対応させて入れる、とやることでidxが自分より小さい数を表すことができる
'''


class Solution2:
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        idx = {}
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in idx:
                idx[sorted_nums[i]] = i

        ans = []
        for i in range(len(nums)):
            ans.append(idx[nums[i]])
        return ans


nums = [6, 5, 4, 8]
sol = Solution2()
print(sol.smallerNumbersThanCurrent(nums))
