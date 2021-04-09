# longest-substring-without-repeating-characters.py
'''
尺取り法（sliding window）だと思ってざっとかけるようになったのは良い。
ただ実行時間が遅い（おそらく len(set(s[left:right]) のところでO（N）が走っているはず。27文字以内に必ずウィンドウが移動するとはいえ最悪ケース（a~zの並びでアルファベットがずっと並んでいる文字列が最悪ケースになりえる）だと27倍近く遅くなる）
いったんほかの回答を見てみて2を書いてみたが、これだとやっぱり 68ms （前のは 250 ms くらい）で4倍くらい速度が違う。とはいえ  60 % faster なのが解せない、ほかのやつ相当早いのか…
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        left = 0
        right = 1
        last = len(s)
        print(last)
        print(len(set(s[left:right])))
        while right <= last and left <= last:
            if (right - left) == len(set(s[left:right])):
                # print('ac case',left,right)
                m = max(m, right - left)
                right += 1
            else:
                left += 1
        return m

    def lengthOfLongestSubstring2(self, s: str) -> int:
        from collections import deque
        q = deque()
        substr = set()
        m = 0
        for c in s:
            while c in substr:
                tail = q.popleft()
                substr.remove(tail)
            q.append(c)
            substr.add(c)
            m = max(m,len(substr))
        return m




testcases ={
    'abcabcbb':3,
    'bbbbb':1,
    'pwwkew':3,
    '':0,
    ' ':1,
    'a':1
}
for s,ans in testcases.items():
    sol = Solution().lengthOfLongestSubstring2(s)
    if sol == ans:
        print(ans,sol,"case",s,"AC")
    else:
        print(ans,sol,"case",s,"WA")

