n = int(input())
S = input()
isIn = False
idx = 0
ns = ''
while idx < len(S):
    c = S[idx]
    if c == '"':
        isIn = not isIn
    elif not isIn and c == ',':
        c = '.'
    ns = ns + c
    idx +=  1
print(ns)

