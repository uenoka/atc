# agc037_a.py
S = input()
ans = []
pre = ""
for c in S:
    if pre == c:
        pre += c
    else:
        print(pre)
        pre = c
        ans.append(pre)
print(ans)
print(len(ans))

