# abc168_b.py
N = int(input())
S = input()
if len(S)<=N:
    print(S)
else:
    print(S[:N]+'...')
