# increasing-decreasing-string.py
'''
とりあえず汚いし遅いけど2秒以内くらいに動作する（N^2logN の計算量）
ソートじゃなくて逆順でFor文を回すとかにしたらちょっと早くなるかも。
あとはCounterとDictとSetでうまいこと検索を速くしてあげるとよさそう。
'''
class Solution:
    def sortString(self, s: str) -> str:
        used = [False]*len(s)
        s = list(s)
        s.sort()
        ans = s[0]
        used[0] = True
        rflg = False
        while False in used:
            for i,c in enumerate(s):
                if not rflg and ans[-1] < c and not used[i]:
                    ans += c
                    used[i]=True
                if rflg and ans[-1] > c and not used[i]:
                    ans += c
                    used[i]=True
            s = list(reversed(s))
            used = list(reversed(used))

            for i,f in enumerate(used):
                if not f:
                    ans += s[i]
                    used[i] = True
                    break
            rflg = not rflg

        return ans

sol = Solution()
s = "leetcode"
print(sol.sortString(s))