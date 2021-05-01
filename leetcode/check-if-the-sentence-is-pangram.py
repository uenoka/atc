# check-if-the-sentence-is-pangram.py
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        sentence = set(sentence)
        for c in alphabet:
            if c not in sentence:
                return False
        return True
    


testcases = [
    "thequickbrownfoxjumpsoverthelazydog",
    'leetcode'
]
for sentence in testcases:
    sol = Solution().checkIfPangram(sentence)
    print(sol)