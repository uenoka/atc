# abc018_2.py
S = list(input())
N = int(input())
for i in range(N):
    l, r = map(int, input().split())
    rev = list(reversed(S[l-1:r]))
    S = S[:l-1] + rev + S[r:]
print("".join(S))
