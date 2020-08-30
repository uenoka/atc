# move-zeroes.py
'''
O(N^2) 解法。バブルソート風。
流石に下から5%という速度。
おそらく0をすべて消す→最後にカウントした分付け加えるというのがよさそう。
'''


class Solution:
    def moveZeroes(self, nums) -> None:
        idx = 0
        zero_idx = len(nums)-1
        while zero_idx - idx >= 0:
            if nums[idx] == 0:
                for i in range(idx+1, len(nums)):
                    nums[i-1] = nums[i]
                nums[len(nums)-1] = 0
                zero_idx -= 1
            else:
                idx += 1

    '''
    効率はそこまで変わらないけど、pop 使うと奇麗にかける
    '''

    def moveZeroes2(self, nums) -> None:
        for i in nums:
            if i == 0:
                nums.pop(nums.index(i))
                nums.append(0)


sol = Solution()
nums = [9, 2, 0, 0, 3, 4, 0, 4, 0, 8]
sol.moveZeroes(nums)
