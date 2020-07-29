# abc089_c.py
import collections
N = int(input())
M = []
for i in range(N):
    c = input()[0]
    if c == 'M' or c == 'A' or c == 'R' or c == 'C' or c == 'H':
        M.append(c)
C = collections.Counter(M)
ans = 0
march = list('MARCH')
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            ans += C[march[i]]*C[march[j]]*C[march[k]]
print(ans)
