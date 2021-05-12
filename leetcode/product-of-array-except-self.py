# product-of-array-except-self.py
'''
0が含まれるので前処理してからというのはできない
→ 前処理で0の場所を管理すればどうにかなる？
0が2個以上ある場合は無条件にすべて0、それ以外は0の場所を管理してあげればよい。
これなんでMediumなんだ…AtCoderでもB問題レベルだと思うが…昔は耕だったみたいな感じかな
'''
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = 1
        zero_idx = -1
        ans = [0]*len(nums)
        for i,v in enumerate(nums):
            if v == 0 and zero_idx != -1:
                return ans
            if v == 0 and zero_idx == -1:
                zero_idx = i
                continue
            all_product *= v
        if zero_idx != -1:
            ans[zero_idx] = all_product
        else:
            for i,v in enumerate(nums):
                ans[i] = all_product//v
        return ans

testcases = [
    [1,2,3,4],
    [-1,1,0,-3,3]
]
for nums in testcases:
    sol = Solution().productExceptSelf(nums)
    print(sol)