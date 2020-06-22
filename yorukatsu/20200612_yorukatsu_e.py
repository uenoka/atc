# 20200612_yorukatsu_e.py
import collections
N = int(input())
A = list(map(int,input().split()))
C = collections.Counter(A)
ans = 0
for i,v in C.items():
    # print(i,v)
    if i!=v:
        if i<v:
            ans += v-i
        else:
            ans += v
print(ans)