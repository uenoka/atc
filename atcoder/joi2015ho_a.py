# joi2015ho_a.py
N, M = map(int,input().split())
P = list(map(int,input().split()))
A = []
B = []
C = []
for i in range(N-1):
    a,b,c = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
route = [0]*(N)
for i in range(M-1):
    start = min(P[i],P[i+1])
    end = max(P[i],P[i+1])
    route[start-1] += 1
    route[end-1] -= 1
ans = 0
cum_sum = 0
for i in range(N-1):
    cum_sum += route[i]
    ans += min(cum_sum * A[i], cum_sum * B[i] + C[i])
print(ans)