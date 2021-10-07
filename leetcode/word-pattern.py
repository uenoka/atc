# word-pattern.py
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        mapping2 = {}
        pattern = list(pattern)
        s= s.split()
        if len(pattern)!=len(s):
            return False
        for x,y in zip(pattern,s):
            if (x in mapping and mapping[x] != y) or (y in mapping2 and mapping2[y] != x):
                return False
            mapping[x] = y
            mapping2[y] = x
        return True

testcases = [
    ["abcdefghijklmnopqrstuvwxyz","a b c d e f g h i j k l m n o p q r s t u v w x y z"],
    ["abba", "dog cat cat fish"],
    ["abba", "dog cat cat dog"],
    ["aaaa", "dog cat cat dog"],
    ["abba", "dog dog dog dog"],
    ["bbbb", "dog dog dog dog"],
]
for pattern,s in testcases:
    sol = Solution().wordPattern(pattern,s)
    print(sol)
