# reverse-string.py
'''
最初の解法
'''


class Solution:
    def reverseString(self, s) -> None:
        for i in range(len(s)):
            if i >= len(s)//2:
                print(s)
                break
            tmp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = tmp


'''
こういう書き方ができるらしい
s[idx], s[len-idx-1] = s[len-idx-1], s[idx]
'''


def reverseString2(self, s) -> None:
    for i in range(len(s)//2):
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]


'''
s[i], s[~i] = s[~i], s[i]
~ はビットの反転らしい。

'''


def reverseString3(self, s) -> None:
    for i in range(len(s)//2):
        s[i], s[~i] = s[~i], s[i]


sol = Solution()
s = ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ",
     "a", " ", "c", "a", "n", "a", "l", ":", " ", "P", "a", "n", "a", "m", "a"]
sol.reverseString(s)
