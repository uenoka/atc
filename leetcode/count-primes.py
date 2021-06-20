# count-primes.py
'''
エラトステネスの篩、線形篩を知っているかどうかのお話
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        def eratosthenes(n):
            return 0
        def liner(N):
            prime_list = []
            lpf = [None] * (N + 1)
            for d in range(2, N):
                if lpf[d] is None:
                    lpf[d] = d
                    prime_list.append(d)
                for p in prime_list:
                    if p * d > N or p > lpf[d]:
                        break
                    lpf[p * d] = p
            return prime_list

        return len(liner(n))

testcases = [
    10,100,1000
]
for n in testcases:
    sol = Solution().countPrimes(n)
    print(sol)