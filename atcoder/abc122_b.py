# abc122_b.py
s = input()
ans = 0
cnt = 0
for i in s:
    if i == "A" or i=="T" or i=="G" or i=="C" :
        cnt+=1
    else:
        if ans<cnt:
            ans=cnt
            cnt=0
if ans<cnt:
    ans=cnt

print(ans)