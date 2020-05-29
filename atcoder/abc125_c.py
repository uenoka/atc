# abc125_c.py
import math
import fractions
from functools import reduce


def gcd(*numbers):
    return reduce(fractions.gcd, numbers)


def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)


N = int(input())
A = [0] + list(map(int, input().split()))
gcd_result = [1]*N
prime_cnt = 0
for i in range(1, N):
    l = A[:i]
    r = A[i+1:]
    print(l, r)
    l_gcd = gcd_list(l)
    r_gcd = gcd_list(r)
    gcd_result[i] = max(l_gcd, r_gcd)


print(gcd_result)
