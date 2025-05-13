N, K = map(int,input().split())
A = list(map(int,input().split()))
l = 0
r = 1
ans = 0
while l < N:
    while r<N and A[r]-A[l] <= K:
        r += 1
    ans += r - l -1
    l+=1
print(ans)
