# abc167_d.py
'''
ほぼおなじ問題が↓らしいので復習がてら解いてみる。
https://atcoder.jp/contests/abc030/tasks/abc030_d
'''
N, K = map(int,input().split())
A = list(map(int,input().split()))
pos = 0
flg = [0] * N
route = [0]
is_ok = 0
while K > 0:
    K-=1
    if flg[pos] == 1 and is_ok==0:
        route = route[route.index(A[pos] - 1):]
        K%=len(route)
        is_ok = 1
#        print("find cycle!:",route)
    flg[pos] = 1
    pos = A[pos] - 1
    route.append(pos)
#    print(route)
print(pos + 1)
