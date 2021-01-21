# reverse-string-ii.py
'''
頭が働いていないとこういうのですらムムムってなるな…
'''


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            print(i)
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)


sol = Solution()
s = "cbadefihgjklnm"
k = 3
print(sol.reverseStr(s, k))
