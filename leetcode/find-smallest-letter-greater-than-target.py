# find-smallest-letter-greater-than-target.py
from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

testcases = [
    [["c", "f", "j"], "a"],
    [["c", "f", "j"], "c"],
    [["c", "f", "j"], "d"],
    [["c", "f", "j"], "g"],
    [["c", "f", "j"], "j"],
]
for letters,target in testcases:
    sol = Solution().nextGreatestLetter(letters, target)
    print(sol)
