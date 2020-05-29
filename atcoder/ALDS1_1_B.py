# ALDS1_1_B.py
import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


N, M = map(int, input().split())
print(gcd(N, M))
