# valid-perfect-square.py
"""
実装としては素因数分解でやったが、2文探索でも可能（こっちのほうがはやい）
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        input : 数字
        return : a^p,b^q,...,c^r を {a:p,b:q,...,c:r} の dict で表したもの
        '''
        def prime_factorization(N):
            pf = {}
            num = 2
            while num**2 <= N:
                cnt = 0
                while N%num == 0:
                    cnt += 1
                    N = N//num
                pf[num] = cnt
                num+=1
            if N!=1:
                pf[N] = 1
            return pf
        pf = prime_factorization(num)
        # print(pf)
        for n,c in pf.items():
            if c%2 != 0:
                return False
        return True


testcases = [1,2,3,4,5,6,7,8,9,1000,10000]
for num in testcases:
    sol = Solution().isPerfectSquare(num)
    print(sol)