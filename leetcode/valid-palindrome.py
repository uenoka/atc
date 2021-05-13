# valid-palindrome.py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def prepare(s):
            alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
            s_trimed = ''
            for c in s:
                if c in alphabet:
                    s_trimed += c
            return s_trimed
        s = prepare(s)
        for i in range(len(s)//2):
            if s[i].lower()!=s[-i-1].lower():
                return False
        return True

testcases = [
    "A man, a plan, a canal: Panama",
    "race a car",
    "0a"
]
for s in testcases:
    sol = Solution().isPalindrome(s)
    print(sol)