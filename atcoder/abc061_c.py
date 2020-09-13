# abc061_c.py
N, K = map(int, input().split())
ans = []
for i in range(N):
    a, b = map(int, input().split())
    tmp = [a]*b
    ans += tmp
ans.sort()
print(ans[K-1])
