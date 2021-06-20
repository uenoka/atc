# factorial-trailing-zeroes.py
'''
5 が何個含まれるかを数えてあげればOK
ただし5の累乗がいくつあるかとかも考えないといけないのでその数がどのくらいかをきちんと把握する
解答見たら5で割り続けるという単純明快回答だった…
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n >= 5:
            ans += n//5
            n //= 5
        return ans


testcases = [
    1,2,3,4,5,6,100,10000
]
for n in testcases:
    sol = Solution().trailingZeroes(n)
    print(sol)