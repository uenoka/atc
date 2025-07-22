N = int(input())
S = []
for _ in range(N):
    S.append(input())
Sij = []

for i in range(N):
    for j in range(N):
        if i!=j:
            Sij.append(S[i]+S[j])
print(len(set(Sij)))