S = input()
T = input()
for i,c in enumerate(S):
    if T[i] != c:
        print(i+1)
        exit()
print(len(S)+1)