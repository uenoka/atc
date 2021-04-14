# check-if-two-string-arrays-are-equivalent.py
class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        return "".join(word1) == "".join(word2)

testcases = [
    [["ab", "c"], ["a", "bc"]],
    [["a", "cb"], ["ab", "c"]]
]
for word1, word2 in testcases:
    sol = Solution().arrayStringsAreEqual(word1, word2)
    print(sol)
