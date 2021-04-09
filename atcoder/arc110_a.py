# arc110_a.py

import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


def calc_lcm(a):
    ans = 1
    for i in a:
        ans *= i
    return ans // gcd_list(a)


N = int(input())
a = [i for i in range(1, N+1)]
lcm = calc_lcm(a)
print(lcm+1)
