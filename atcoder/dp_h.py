# dp_h.py
'''
最初はDFSだからと思って再帰的に書こうとしたけど、こんがらがって詰んだ。
考え方まではあってたけどちょっと実装が弱いなぁ。
解説読んだら数行で書いていてめちゃくちゃ奇麗でびっくりした、こういうのがぱっとできるといいなぁ。
'''


def printdp():
    for i in dp:
        print(i)


mod = 10**9+7
H, W = map(int, input().split())
glid = [["#"]*(W+1)]
dirs = [[1, 0], [0, 1]]

for i in range(1, H+1):
    row = list(input())
    row = ["#"] + row

    glid.append(row)
dp = [[0 for i in range(W+1)] for j in range(H+1)]
dp[1][1] = 1

for i in range(1, H+1):
    for j in range(1, W+1):
        if not(i == 1 and j == 1):
            if glid[i][j] == "#":
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % mod

print(dp[H][W])
