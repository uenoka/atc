# abc167_a.py
S = input()
T = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    if T == S+i:
        print('Yes')
        exit()
print('No')