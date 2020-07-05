# abc082_b.py
S = input()
T = input()

S = sorted(S, reverse=False)
T = sorted(T, reverse=True)
if S >= T:
    print('No')
else:
    print('Yes')
