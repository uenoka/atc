# NTL_1_B.py
def _pow(x, n, mod):
    if n == 0:
        return 1
    if n % 2 == 0:
        return _pow(x**2, n//2, mod) % mod
    else:
        return x * _pow(x**2, (n-1)//2, mod) % mod

M,N = map(int,input().split())
mod = 10**9+7
print(_pow(M, N,mod = mod))

