# abc084_b.py
A, B = map(int,input().split())
S = input()
ans ='Yes'
for i,c in enumerate(S):
    if i<A and c.isdecimal():
        continue
    elif i== A and c =="-":
        continue
    elif  i>A and c.isdecimal():
        continue
    else:
        ans = 'No'
        break
print(ans)