# abc021_d.py
def calc(n,k,ans):
    if k <= 0:
        return 1
    for i in range(k):
        ans += calc(n,k-i-1,ans)
    return ans


N = int(input())
K = int(input())
ans = 0
print(calc(N,K,ans))