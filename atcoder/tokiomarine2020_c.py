# tokiomarine2020_c.py
import math
N, K = map(int,input().split())
A = list(map(int,input().split()))
ans = [0]*N
for i in range(K):
    for i,v in enumerate(A):
        ans[i] = 1
        for j in range(max(0,math.ceil(i+1-v-0.5)),min(N,math.floor(i+1+v+0.5))):
            # print(i,j)
            print(max(0,math.floor(i+1-v-0.5)),min(N,math.ceil(i+1+v+0.5)))
            if j+i<N:
                ans[j+i]+=1
            print(ans)
    A = ans
print(A)