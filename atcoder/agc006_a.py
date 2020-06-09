# agc006_a.py
N = int(input())
S = list(input())
T = list(input())
ans = N*2
for i in range(N):
    # print(i,S[N-1-i:] , T[:i+1])
    if S[N-1-i:] == T[:i+1]:
        # print("find")
        ans = N*2-(i+1)
print(ans)
