# abc125_c.py
import math
import fractions
from functools import reduce
def gcd(*numbers):
    return reduce(fractions.gcd, numbers)
def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

def is_prime2(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    i = 1
    while i**2 <= N:
        if N%i == 0:
            return True
        i += 1
    return False

N = int(input())
A = list(map(int,input().split()))
max_gcd = 1
# print("A : ",A)
prime_cnt = 0
for i in range(N-1):
    A_tmp = A[:i]+A[i+1:]
    target = gcd_list(A_tmp)
    if max_gcd < target:
        max_gcd = target
print(max_gcd)
