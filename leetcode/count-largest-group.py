# count-largest-group.py

class Solution:
    def countLargestGroup(self, n: int):
        import collections
        ans = [0]*37
        for i in range(1, n+1):
            s = str(i)
            tmp = 0
            for j in s:
                tmp += int(j)
            ans[tmp] += 1
        C = collections.Counter(ans)
        return C[max(C.keys())]


sol = Solution()
n = 13
print(sol.countLargestGroup(n))
