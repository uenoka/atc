# arc104_b.py
'''
T=奇数の時明らかに存在しないから見なくていい。
A:T,G:Cが同じになっているものが答え。
連続する文字列なのでO(N!)になってしまうので、それをどう解決するか?
累積和的に、A,T,G,Cの数を管理すれば行けそう??
'''
N, S = input().split()
N = int(N)
Asum = [0]
Acnt = 0
Tsum = [0]
Tcnt = 0
Gsum = [0]
Gcnt = 0
Csum = [0]
Ccnt = 0
for i, c in enumerate(S):
    if c == 'A':
        Acnt += 1
    if c == 'T':
        Tcnt += 1
    if c == 'G':
        Gcnt += 1
    if c == 'C':
        Ccnt += 1
    Csum.append(Ccnt)
    Asum.append(Acnt)
    Tsum.append(Tcnt)
    Gsum.append(Gcnt)

ans = 0
for i in range(N):
    for j in range(i+1, N):
        if Asum[j+1]-Asum[i] == Tsum[j+1]-Tsum[i] and Gsum[j+1]-Gsum[i] == Csum[j+1]-Csum[i]:
            ans += 1
print(ans)
