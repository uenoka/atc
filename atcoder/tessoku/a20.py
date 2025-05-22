'''

# 問題概要

LCS(longest common substring),最長共通部分列問題

# 考察
縦と横に入力の文字列を展開した2次元配列を持って、DPをする。
なぜ斜めを見るのかみたいなのがちょっとよくわからん。(これは本の解説分かりづらくないか…)
'''

def fprint(dp):
    for i in dp:
        print(i)
S = input()
T = input()
DP = [[0 for _ in range(len(S)+1)] for _ in range(len(T)+1)]
for i in range(1,len(T)+1):
    for j in range(1,len(S)+1):
        if T[i-1] == S[j-1]:
            DP[i][j] = max(DP[i-1][j],DP[i][j-1],DP[i-1][j-1] + 1)
        else:
            DP[i][j] = max(DP[i-1][j],DP[i][j-1])
print(max(DP[len(T)]))