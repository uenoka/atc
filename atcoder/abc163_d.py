# abc163_d.py
# 結局K(10^100)+...という形になるから、nCk をやる,重複を考えて排除するという形になりそう
# あとはそれをどうやるのかが問題。これは結構 10^9+7 系問題の練習になりそう

N, K = map(int,input().split())
mod = 10**9+7
ans = 0
for i in range(K,N+2):
    ans += i*(N+1-i)+1
print(ans%mod)