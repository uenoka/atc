# abc178_c.py
import math
def fact(n,r):
    from math import factorial
    return factorial(n) // factorial(r) // factorial(n - r)


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p


N = int(input())
if N<2:
    print(0)
    exit()
mod = 10**9+7
b=fact(N,N-2)

a=pow(9,N-2,mod)
print(int(2*a*b)%mod)
