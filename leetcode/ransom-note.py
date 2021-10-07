# ransom-note.py
import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = collections.Counter(list(magazine))
        ransomNote = collections.Counter(list(ransomNote))
        for c,v in ransomNote.items():
            if magazine[c] < v:
                return False
        return True

testcases = [
    ["a", "b"],
    ["aa", "ab"],
    ["aa", "aab"],
    ["aab","baa"],
    ["abc","aabbddcc"]
]
for ransomNote, magazine in testcases:
    sol = Solution().canConstruct(ransomNote, magazine)
    print(sol)
