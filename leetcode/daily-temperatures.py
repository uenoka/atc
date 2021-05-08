# daily-temperatures.py
'''
普通に考えたらO(N^2)だけど、さてどうするか。
うまいこと逆順にソートしていくことでできないか？
もしくは Two pointers でやっていけそう？
stack に入れていく解法面白いなーーーー！！！すごい。結局解けなくて解法見たけどこれは思いつかんかった…
'''
from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0]*len(T)
        stack = []
        for i,t in enumerate(T):
            while stack and stack[-1][1]< t:
                idx,_ = stack.pop()
                ans[idx] = i-idx
            stack.append([i, t])
        return ans

testcases = [
    [31, 31, 31, 32, 33, 33, 33, 32, 32, 31, 32, 33, 32],
    [73, 74, 75, 71, 69, 72, 76, 73],
    [73, 74, 75, 71, 69, 72],
]
for T in testcases:
    sol = Solution().dailyTemperatures(T)
    print(sol)

