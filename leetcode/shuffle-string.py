# shuffle-string.py
class Solution:
    def restoreString(self, s, indices) -> str:
        ans = [""]*len(indices)
        for i in range(len(indices)):
            ans[indices[i]] = s[i]
        return "".join(ans)


sol = Solution()
s = 'abc'
indices = [0, 1, 2]
print(sol.restoreString(s, indices))
