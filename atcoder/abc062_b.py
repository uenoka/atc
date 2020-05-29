# abc062_b.py
H, W = map(int,input().split())
S = ["#"*(W+2)]
for i in range(H):
    S.append("#"+input()+"#")
S.append("#"*(W+2))
for c in S:
    print(c)

