# find-numbers-with-even-number-of-digits.py
import math


class Solution:
    def findNumbers(self, nums) -> int:
        ans = 0
        for i in nums:
            s = str(i)
            if len(s) % 2 == 0:
                ans += 1
        return ans
    '''
    log を使うことで桁数を判定できるから少し早いっぽい。
    とはいえ60ms -> 56 ms だからオーダー変わるほどではななさそう。
    '''

    def findNumbers2(self, nums) -> int:
        result = 0
        for num in nums:
            if(int(math.log10(num)) % 2 == 1):
                result += 1
        return result


sol = Solution()
nums = [12, 345, 2, 6, 7896]
print(sol.findNumbers(nums))
