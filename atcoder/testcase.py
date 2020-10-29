# testcase.py
'''
create test case 
'''
import random
N = 100
M = 10**5
print(N, M)
for i in range(N):
    print(random.randrange(1, N), random.randrange(1, M//72))
