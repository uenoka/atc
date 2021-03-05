# string-to-integer-atoi.py
'''
アルゴリズムというよりはどちらかというと出された仕様をしっかり把握して、
あり得る入力からコーナーケースをちゃんと見つけられるかといった問題っぽい。
そういう意味ではいい問題だと思うがMediumになるかというとうーんって感じかな？（" "の入力例とかは忘れられそうだからまぁ有りなのかもしれないけれど。）
あとはどちらかというとちょっと面倒なコードをきれいに書けるかとかも見られそうだなぁ。
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        s= s.strip()
        if len(s)==0 :
            return 0
        start = 0
        if s[0]=="-" or s[0]=="+":
            start += 1
        isNegative = True if s[0]=="-" else False
        numbers = set([str(i) for i in range(10)])
        ans = ""
        for c in s[start:]:
            if c in numbers:
                if len(ans) == 0 and c=="0":
                    continue
                else:
                    ans+= c
            else:
                break
            # print(ans,isNegative)
        ans = int(ans) if len(ans)>0 else 0
        ans = -ans if isNegative else ans
        if ans > 2**31 -1:
            ans = 2**31 -1
        elif  ans < -(2**31):
            ans = -(2**31)
        return ans


testcases =[
    # "     aa                 ",
    # "   -1234 aaavvv",
    # "-1234-1234 aaavvv",
    # "1234rerere",
    # "99999999999999rerere",
    # "             -99999999999999rerere",
    "",
    " "
]
for s in testcases:
    sol = Solution().myAtoi(s)
    print(sol)