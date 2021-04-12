# truncate-sentence.py
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        def truncateSentenceSplit(s, k):
            s = s.split(' ')
            return ' '.join(s[:k])
        return truncateSentenceSplit(s, k)

testcases = [
    ["Hello how are you Contestant", 4],
    ["What is the solution to this problem", 4],
    ["chopper is not a tanuki", 5]

]

for s,k in testcases:
    sol = Solution().truncateSentence(s,k)
    print(sol)
