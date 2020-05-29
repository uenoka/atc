# agc003_a.py
S = input()
direct = [0]*4
for i in S:
    if i == "W":
        direct[0] = 1
    elif i == "E":
        direct[1] = 1
    elif i == "S":
        direct[2] = 1
    elif i == "N":
        direct[3] = 1
if direct[0] == direct[1] and direct[3] == direct[2]:
    print('Yes')
    exit()
print('No')
