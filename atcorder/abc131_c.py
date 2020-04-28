# abc131_c.py
'''
M を C,D でそれぞれ割り切れるもの
N を CD の最小公倍数で割り切れるもの
とすると
(B - A + 1) - (M - N)
で求められるはず
'''
import math
import fractions
from functools import reduce
def gcd(*numbers):
    return reduce(fractions.gcd, numbers)
def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

def lcm(a,b):
    return (a*b)//gcd(a,b)

A,B,C,D = map(int,input().split())
r = (B - A + 1)
M = math.ceil(r/C) + math.ceil(r/D)
N = math.ceil(r/lcm(C,D))
print(r-M+N)