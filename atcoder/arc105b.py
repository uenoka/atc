# arc105_b.py
N = int(input())
A = list(map(int,input().split()))
import math
from functools import reduce
def gcd(*numbers):
    return reduce(math.gcd, numbers)
def gcd_list(numbers):
    return reduce(math.gcd, numbers)

print(gcd_list(A))