'''
input : 数字
return : a^p,b^q,...,c^r を {a:p,b:q,...,c:r} の dict で表したもの
'''
import time
s = time.time()
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
    return pf

N=10**18
prime_factorization(N)
g = time.time()
print(g-s)