# determine-if-string-halves-are-alike.py
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        a = a.lower()
        b = b.lower()
        target = set(['a','e','i','o','u'])
        acnt = 0
        for c in a:
            if c in target:
                acnt+=1
        bcnt = 0
        for c in b:
            if c in target:
                bcnt += 1
        return acnt == bcnt

testcases = [
    "AbCdEfGh",
    "MerryChristmas",
    "book", 
    "textbook",
    "Uo"
]
for s in testcases:
    sol = Solution().halvesAreAlike(s)
    print(sol)
