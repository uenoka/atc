# abc131_c.py
'''
M を C,D でそれぞれ割り切れるもの
N を CD の最小公倍数で割り切れるもの
とすると
(B - A + 1) - (M - N)
で求められるはず
'''
import math
from  fractions import gcd

def lcm(a,b):
    return (a*b)//gcd(a,b)

A,B,C,D = map(int,input().split())
d_cnt = B//D-(A-1)//D
c_cnt = B//C-(A-1)//C
cd = lcm(C,D)
cd_cnt = B//cd-(A-1)//cd
print(B-A+1-(c_cnt+d_cnt-cd_cnt))

