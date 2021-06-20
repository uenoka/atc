# longest-common-prefix.py
from typing import List
'''
1つ目と2つ目でプレフィックスを探す → そのプレフィックスが3つ目以降であるかどうか、なければ小さくしていくを繰り返す。
0になったら終わらせる方向で実装。
発想としては LCP(str1,str2,...,strn) = LCP(LCP(LCP(str1,str2)str3),...,strn) と同等。
計算量はO(S) (S = strs に含まれる文字数の総和)
ただしこの場合、strs の最後に短い文字列、ほかのstrはprefixが長い状態となると無駄が生じやすい。
なので、strsの各文字のカラムを縦で比較していく方法もデータの状態によっては有効になる。
またそのほかに
LCP(str1,str2,...,strn) = LCP(LCP(S1,S2,...,Sn/2),LCP(Sn/2+1,Sn/2+2,...,Sn))
とできることから分割統治法でも実装できる。
また最初の文字列の中にプレフィックスがあるので二分探索する方法もある。
'''
class Solution:
    def prefix(self,str1,str2):
        ret = ''
        for i in range(min(len(str1),len(str2))):
            if str1[i] == str2[i]:
                ret += str1[i]
            else:
                break
        return ret
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)<2:return strs[0]
        ans = self.prefix(strs[0],strs[1])
        if len(ans) == 0:
            return "" 
        for str in strs[2:]:
            if len(ans)==0:
                break
            ans = self.prefix(str,ans)
        return ans

testcases =[
        ["dog","racecar","car"],
        ["flower","flow","flight"]
    ]
for strs in testcases:
    sol = Solution().longestCommonPrefix(strs)
    print(sol)