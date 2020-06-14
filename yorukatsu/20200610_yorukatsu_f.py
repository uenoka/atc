# 20200610_yorukatsu_f.py
S = input()
cnt = 0
for i,c in enumerate(S):
    if i>0:
        if c!=S[i-1]:
            cnt += 1
print(cnt)