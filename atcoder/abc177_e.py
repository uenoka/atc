# abc177_e.py
import math
from functools import reduce
def gcd(*numbers):
    return reduce(math.gcd, numbers)
def gcd_list(numbers):
    return reduce(math.gcd, numbers)

N = int(input())
A = list(map(int,input().split()))
if gcd_list(A)==1:
    pass
else:
    print("not coprime")
