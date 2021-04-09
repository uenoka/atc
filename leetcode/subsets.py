# subsets.py
'''
基本はけんちょんさんの再帰の書き方を踏襲すればいけそう。
クラスの中でそれをどうやるのかってのが分かるとできそうだからいい練習になる
itertools が楽過ぎてこれでやってしまう…他の解き方ができるといいなぁ。
'''


class Solution:
    def subsets(self, nums):
        import itertools
        status = [(0, 1) for _ in range(len(nums))]
        state = list(itertools.product(*status))
        ans = []
        for s in state:
            tmp = []
            for i,v in enumerate(s):
                if v==1:
                    tmp.append(nums[i])
            ans.append(tmp)
        return ans
nums = [1,2,3,4,5,6,7]
sol = Solution().subsets(nums)
print(sol)
