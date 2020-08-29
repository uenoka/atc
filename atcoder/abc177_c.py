# abc177_c.py
def solve():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    mod = 10**9+7
    for i in range(N-1):
        for j in range(i+1,N):
            if i != j:
                ans+=A[i]*A[j]
                ans%=mod
    return ans%mod

print(solve())