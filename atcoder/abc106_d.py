# abc106_d.py
N, M, Q = map(int, input().split())
cumsum = [0]*(N+1)
for i in range(M):
    l, r = map(int, input().split())
    cumsum[l] += 1
    cumsum[r] -= 1
    print(cumsum)
