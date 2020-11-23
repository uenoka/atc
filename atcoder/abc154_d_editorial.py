

X# abc154_d_editorial.py
n,k = map(int,input().split())
p = list(map(int,input().split()))
 
exp = [(1+i)/2 for i in p]
 
s = []
sums = 0
for i in exp:
    sums += i
    s.append(sums)
 
exps = [s[k-1]]
print(exps)
print(s)
for i in range(k,len(p)):
    exps.append(s[i] - s[i-k])

print(exps)

print(max(exps))