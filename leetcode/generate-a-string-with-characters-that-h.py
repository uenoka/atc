# generate-a-string-with-characters-that-have-odd-counts.py
'''
こんなのでいいのか…?系の問題だけど、結局偶数の時は奇数+奇数に分解できるからそれぞれに a, b を割り当ててあげればいい、
奇数の時はそのまま a だけで出力してあげればいい。
'''


class Solution:
    def generateTheString(self, n: int) -> str:
        ans = []
        if n % 2 == 0:
            ans += (["a"]*(n-1))
            ans += (["b"])
        else:
            ans += ["a"]*(n-2)
        return "".join(ans)


sol = Solution()
n = 7
print(sol.generateTheString(n))
