# abc103_b.py
S = input()
T = input()
ans = "No"
for i,c in enumerate(S):
    if T == S[i+1:]+S[:i+1]:
        ans= "Yes"
print(ans)