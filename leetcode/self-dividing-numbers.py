# self-dividing-numbers.py
'''
あまりきれいじゃないなぁ…
計算量もあまりよくない、これうまいやりかたあるのかな?
'''


class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        ans = []
        for i in range(left, right+1):
            digits = list(str(i))
            for j in digits:
                flg = True
                if int(j) == 0 or i % int(j) != 0:
                    flg = False
                    break
            if flg:
                ans.append(i)
        return ans


sol = Solution()
left = 1
right = 22
print(sol.selfDividingNumbers(left, right))
