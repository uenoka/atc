# permutations.py
'''
itertools 使ったらつまらないので自分で実装する
'''

import itertools


class Solution:
    def permute(self, nums):
        pass

    def permute_itertools(self, nums):
        target = itertools.permutations(nums)
        return target
