# number-complement.py
'''
バイナリを逆にした数を出力する
'''


class Solution:
    def findComplement(self, num: int):
        numstr = format(num, "b")
        print(numstr)
        ans = 0
        for i, c in enumerate(numstr):
            if c == '0':
                ans += 2**(len(numstr)-i-1)
        return ans


sol = Solution()
nums = [5, 6, 12, 31, 43]
for num in nums:
    print(sol.findComplement(num))
