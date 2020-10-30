# testcase.py
'''
create test case 
'''
import random
N = 25
M = 30
print(N, M)
for i in range(M):
    bef = random.randrange(1, N)
    aft = random.randrange(1, N)
    while bef == aft:
        bef = random.randrange(1, N)
        aft = random.randrange(1, N)
    print(bef, aft)
