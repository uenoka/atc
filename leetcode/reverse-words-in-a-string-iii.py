# reverse-words-in-a-string-iii.py
class Solution:
    def reverseWords(self, s: str) -> str:
        rev = []
        s = s.split(" ")
        for i in s:
            rev.append("".join(list(reversed(i))))
        return " ".join(rev)


sol = Solution()
s = "Let's take LeetCode contest"
print(sol.reverseWords(s))
