# arc013_2.py
'''
縦横奥行が別の並びでも、入れ方を変えれば大丈夫になる。
→入力の3値をソートしてあげればよい。
'''
C = int(input())
N = 0
M = 0
L = 0
for i in range(C):
    n,m,l = sorted(list(map(int,input().split())))
    if n > N:
        N = n
    if m > M:
        M = m
    if l > L:
        L = l
print(N*M*L)