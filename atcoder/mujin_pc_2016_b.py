# mujin_pc_2016_b.py

import math
oa,ab,bc = map(int,input().split())
ans = 0
if oa > ab + bc:
    ans = (oa + ab + bc)**2*math.pi-(oa - ab - bc)**2*math.pi
else:
    ans = (oa + ab + bc)**2*math.pi
print(ans)