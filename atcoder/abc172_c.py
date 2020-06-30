# abc172_c.py
'''
尺取り法、二分探索、両方良問なので両方で解けるようにする。
'''
N, M ,K= map(int,input().split())
A = [0] + list(map(int,input().split()))
B = list(map(int,input().split()))
ans = 0
cnt = []
b_idx = M-1
# A を１冊ずつ増やす→B の読める場所を後ろにずらしていくイメージで実装する
# 両方累積和で管理して、計算を減らす(Bは特に後ろにずらすと再計算が必要) 
b_cum = []
cum = 0
for b in B:
    cum += b
    b_cum.append(cum)
a_sum = 0
for i,a in enumerate(A):
    a_sum += a
    if a_sum > K:
        break
    while b_idx >= 0 and a_sum + b_cum[b_idx] > K:
        b_idx -= 1
    ans = max(ans, i + b_idx + 1)
print(ans)