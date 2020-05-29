# abc167_b.py
A,B,C,K = map(int,input().split())
ans = 0
ans += min(A,K)
K = K-A
K -= B
if K>0:
    ans -= min(C,K)
print(ans)