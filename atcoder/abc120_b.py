# abc120_b.py
import fractions 
from functools import reduce
def gcd(*numbers):
    return reduce(fractions.gcd, numbers)
def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

A, B, K = map(int,input().split())
cnt = 0
_max = gcd(A,B)
while _max>=0:
    if A%_max==0 and B%_max==0:
        cnt += 1
        if cnt == K:
            print(_max)
            exit()
    _max -=1
