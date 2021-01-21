# range-sum-query-immutable.py
'''
DP の検索で出てきたけど、DP というより累積和をインスタンス初期化した時に持っておいて
sumRange で O(1) で返せるようにしましょうという問題っぽい。
mutable はセグメントツリーでの実装になるのかな? ( https://leetcode.com/problems/range-sum-query-mutable/ )
'''


class NumArray:

    def __init__(self, nums):
        length = len(nums)
        self.cumsum = [0]*(length+1)
        tmp = 0
        for i in range(length):
            tmp += nums[i]
            self.cumsum[i+1] = tmp
        print(self.cumsum)

    def sumRange(self, i: int, j: int) -> int:
        return self.cumsum[j+1] - self.cumsum[i]


nums = [-2, 0, 3, -5, 2, -1]
sol = NumArray(nums)
q = [[0, 2], [2, 5], [0, 5]]
for i, j in q:
    print(sol.sumRange(i, j))
