# paiza_b040.py
'''
コーナーケースで間違ってるっぽいがどこがコーナーケースかわからない…
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
N, table = input().split()
N = int(N)
S = input()
ans = ""
for i in range(N):
    ans = ""
    for c in S:
        idx = table.find(c)
        print(idx)
        if c == " ":
            ans += " "
        else:
            ans += alphabet[idx]
    S = ans

print(ans)
