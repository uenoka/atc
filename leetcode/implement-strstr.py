# implement-strstr.py
'''
とりあえずBruteforce的に実装してみる。
Needleの長さ以下を探索する意味はないからその分を飛ばしって行ったらそれだけで 28ms 85% faster
ただそれだけの問題だったっぽい？？
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        offset = len(needle)
        for i in range(len(haystack)-offset+1):
            if haystack[i:i+offset] == needle:
                return i
        return -1

testcases = [
    ["aaaaa", "bba"]
    ,["abcdefg","cdef"]
    ,["hello","ll"]
]
for haystack,needle in testcases:
    sol = Solution().strStr(haystack, needle)
    print(sol)