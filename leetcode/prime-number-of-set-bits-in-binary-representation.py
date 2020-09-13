# prime-number-of-set-bits-in-binary-representation.py

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        ans = 0
        for i in range(L, R+1):
            digit = format(i, "b")
            cnt = digit.count("1")
            if self.is_prime(cnt):
                ans += 1
        return ans

    def is_prime(self, n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True


sol = Solution()
# L = 6
# R = 10
L = 10
R = 15
print(sol.countPrimeSetBits(L, R))
