# find-n-unique-integers-sum-up-to-zero.py
'''
一番簡単なのは、偶数個の時は正負逆転させる、奇数個の時は0をそれに加える。
ランダムにしないといけない要件はないからそれでいいかな?面白みはないけど。
'''


class Solution:
    def sumZero2(self, n: int):
        al = []
        al = list(range(0-int(n/2), int(n/2+1)))
        if n % 2 == 0:
            al.remove(0)
        return al

    def sumZero(self, n: int):
        ans = []
        if n % 2 == 0:
            ans += self.makeBalancedNumbers(n)
        else:
            ans.append(0)
            ans += self.makeBalancedNumbers(n)
        return ans

    def makeBalancedNumbers(self, n: int):
        ans = []
        for i in range(1, n//2+1):
            ans.append(i)
            ans.append(-i)
            print(ans)
        return ans


sol = Solution()
n = 4
print(sol.sumZero2(n))
n = 5
print(sol.sumZero2(n))
