# occurrences-after-bigram.py

class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        textarr = text.split(" ")
        print(textarr)
        ans = []
        for i in range(len(textarr)-2):
            if textarr[i] == first and textarr[i+1] == second:
                print(textarr[i], textarr[i+1], textarr[i+2])
                ans.append(textarr[i+2])

        return ans


sol = Solution()
# text = "ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv ypkk"
# first = "lnlqhmaohv"
# second = "ypkk"
text = "we will we will rock you"
first = "we"
second = "will"

print(sol.findOcurrences(text, first, second))
