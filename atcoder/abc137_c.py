# bc137_c.py
import math
def nCr(n,r):
    if n < 2:
        return 0
    ans = int(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))
    return ans 
import collections
N = int(input())
L = []
for i in range(N):
    S = input()
    S = sorted(S)
    L.append(str(S))
C = collections.Counter(L)
ans = 0
for i in C.values():
    ans += nCr(i,2)
print(ans)