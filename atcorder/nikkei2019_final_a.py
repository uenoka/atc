# nikkei2019_final_a.py
'''
累積和の基本問題
累積和楽しくなってきた。
'''
N = int(input())
A = list(map(int,input().split()))
c_sum = [0]*(N+1)
_sum = 0
for i,v in enumerate(A):
    _sum += v
    c_sum[i+1] = _sum
#print(c_sum)
for i in range(N):
    ans = 0
    for j in range(N-i):
#        print(c_sum[i+j], c_sum[i])
        if ans < c_sum[i+j+1] - c_sum[j]:
            ans = c_sum[i+j+1] - c_sum[j]
    print(ans)
