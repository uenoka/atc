# keyboard-row.py
class Solution:
    def findWords(self, words):
        top = set(list("qwertyuiopQWERTYUIOP"))
        middle = set(list("asdfghjklASDFGHJKL"))
        bottom = set(list("zxcvbnmZXCVBNM"))
        ans = []
        for word in words:
            multirow = [0, 0, 0]
            for c in word:
                if c in top:
                    multirow[0] += 1
                if c in middle:
                    multirow[1] += 1
                if c in bottom:
                    multirow[2] += 1
            if len(word) in multirow:
                ans.append(word)
        return ans


sol = Solution()
arr = ["Hello", "Alaska", "Dad", "Peace"]
print(sol.findWords(arr))
