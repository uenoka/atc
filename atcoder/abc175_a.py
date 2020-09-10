# # abc175_a.py
S = input()
ans  = [0]
cnt = 0
for i in S:
    if i =="S":
        ans.append(cnt)
        cnt = 0
    else:
        cnt+=1
print(max(max(ans),cnt))
