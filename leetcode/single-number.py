# single-number.py
import collections

'''
普通にCounterを使って1つのやつを見つける愚直解法
'''


class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    def singleNumber(self, nums) -> int:
        C = collections.Counter(nums)
        for i, v in C.items():
            if v == 1:
                return i
        return 0

    '''
    重複を削除した要素の和 * 2 から要素の和を引くことでO(1)で求めることもできる（和をとるときにO(N)?）
    '''

    def singleNumber2(self, nums) -> int:
        return 2*sum(set(nums))-sum(nums)


sol = Solution()
nums = [9, 2, 2, 3, 3]
print(sol.singleNumber2(nums))
