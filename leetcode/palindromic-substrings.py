# palindromic-substrings.py
'''
単純に2重ループで実装するとTLEになる。
さてどうしたものか。
2重ループで文字列を全探索していって、回文かどうかの判定を一つ小さくした文字列が回文かつ左右先端の文字が同じ化で判定する。
で i,j をメモっておくことで回文判定を軽くする
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        self.parindrome = set()
        def is_palindorome(i,j):
            if i>=j :
                self.parindrome.add((i,j))
                return True
            if (i,j) in self.parindrome:
                return True
            if i >= 0 and j<len(s) and s[i] == s[j] and is_palindorome(i+1, j-1):
                self.parindrome.add((i,j))
                return True
            return False
        ans = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if is_palindorome(i, j):
                    ans+=1
        return ans

testcases = [
    "aabbccbbaa"
]
for s in testcases:
    sol = Solution().countSubstrings(s)
    print(sol)