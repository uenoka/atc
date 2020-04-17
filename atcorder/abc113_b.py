# abc113_b.py
N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
lowest = 10**9
ans = 0
for i in range(N):
    tmperture = abs(A-(T-H[i]*0.006))
    if abs(tmperture) < lowest:
        ans = i + 1
        lowest = tmperture
print(ans)