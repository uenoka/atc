# aclbc_b.py
A,B,C,D = map(int,input().split())
ans = "No"
if C<A :
    if A<=D:
        ans = "Yes"
else:
    if C<=B:
        ans = "Yes"
print(ans)
