# add-digits.py
'''
簡単な再帰でよさそう。
num の制限が 2^31-1 なのでどのくらいの計算量なんだろう？
Digit root という O(1) の問題らしい。
-> num の各桁を足し合わせた時に、 9 の倍数だったら9を、それ以外だったら9で割ったあまりを求めることで求まるとのこと。
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        ans = 0
        for i in str(num):
            ans += int(i)
        return self.addDigits(ans)

testcases = [
    1,2,3,4,3245,432,1234,4324,234,33,4343
]
for num in testcases:
    sol = Solution().addDigits(num)
    print(sol)