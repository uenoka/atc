# abc179_c.py
import math
N = int(input())
cnt = 0
for i in range(1,N+1):
    if i*(N//i)==N:
        # print(i,N//i-1)
        cnt += N//i-1
    else:
        cnt += N//i
        # print(i,N//i)
print(cnt)
