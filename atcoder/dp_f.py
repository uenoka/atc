# dp_f.py
def printdp():
    for i in dp:
        print(i)


S = input()
T = input()
slen = len(S)
tlen = len(T)
dp = [['' for i in range(tlen+1)] for j in range(slen+1)]
# print(dp)

for i in range(1, slen+1):
    for j in range(1, tlen+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j-1]+S[i-1]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
# printdp()
print(dp[slen][tlen])
