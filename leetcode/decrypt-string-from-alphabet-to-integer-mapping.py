# decrypt-string-from-alphabet-to-integer-mapping.py
'''
そんなむずくはないけどDictの練習みたいな感じか、それか正規表現ゴリゴリのほうが速いかな？
いずれにせよ面倒系…笑
'''
class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = {
            "10#":"j",
            "11#":"k",
            "12#":"l",
            "13#":"m",
            "14#":"n",
            "15#":"o",
            "16#":"p",
            "17#":"q",
            "18#":"r",
            "19#":"s",
            "20#":"t",
            "21#":"u",
            "22#":"v",
            "23#":"w",
            "24#":"x",
            "25#":"y",
            "26#":"z",
            "1":"a",
            "2":"b",
            "3":"c",
            "4":"d",
            "5":"e",
            "6":"f",
            "7":"g",
            "8":"h",
            "9":"i"
        }
        for n,c in alphabet.items():
            s = s.replace(n,c)
        return s

sol = Solution()
s = "12341234"
print(sol.freqAlphabets(s))
