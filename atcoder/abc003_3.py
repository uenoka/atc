# abc003_3.py
N, K = map(int,input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
A = A[:K]
A.sort()
ans = 0
for i in range(K):
    ans = max(ans,(ans+A[i])/2)
print(ans)