# sum-of-digits-in-base-k.py
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def toKdigit(n, k):
            digit = 1
            ret = 0
            while n >= k:
                d = n%k
                n //= k
                ret += d*digit
                digit *= 10
            d = n % k
            ret += d*digit
            return ret
        kdigit = toKdigit(n,k)
        print(kdigit)
        ans = 0 
        for i in str(kdigit):
            ans += int(i)
        return ans

testcases = [
    [34,6],
    [100,3]
]

for n,k in testcases:
    sol = Solution().sumBase(n,k)
    print(sol)
