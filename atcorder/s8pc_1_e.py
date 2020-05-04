# s8pc_1_e.py
'''
それぞれの町の距離を mod10**9+7 で用意しておいて、
最後に足し合わせて、もう一度 mod とってあげれば行けそう？
'''
N, Q = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))
modint = 10**9+7
mod_dist =[0]
dist = 0
for i in range(1,N):
    dist += pow(A[i-1],A[i],modint)
    mod_dist.append(dist)

# print(mod_dist)
ans = 0
# print(Q)
start = 0
for i in C:
    # mod_dist をそれまでの距離の累積和テーブルにして、abs(mod_dist[end]-mod_dist[start])
    # にしてあげれば行けそう。あと少し！！
    ans += abs(mod_dist[start]-mod_dist[i-1])
    start = i-1
ans += abs(mod_dist[start]-mod_dist[0])
print(ans % modint)