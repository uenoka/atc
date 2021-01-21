# build-an-array-with-stack-operations.py
'''
概要
[1,2,3,4,... ,N] の N 要素の配列から Push , Pop を使って target を生成せよ。
簡単に考えると、
ループ :    1    2    3
要素   :    1         3
となっているときに、ある要素はpushのみ（1, 3）、ない要素は push, pop という感じがよさそう。
'''
class Solution:
    def buildArray(self, target, n: int):
        uniqueTarget = set(target)
        ans = []
        for i in range(1,n+1):
            if i in uniqueTarget:
                ans.append("Push")
            else:
                ans.append("Push")
                ans.append("Pop")
            if i>=max(uniqueTarget):
                break
        return ans

sol = Solution()
target = [1,3]
n = 3
print(sol.buildArray(target,n))